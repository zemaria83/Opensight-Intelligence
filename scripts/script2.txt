import argparse
import time
import dns.resolver
import dns.exception

def load_subdomains(file_path: str) -> list[str]:
    """Carrega subdomínios de um ficheiro de texto (um por linha)."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            subs = []
            for line in f:
                s = line.strip().strip(".")
                if s and not s.startswith("#"):
                    subs.append(s)
        # remover duplicados mantendo ordem
        seen = set()
        cleaned = []
        for s in subs:
            if s not in seen:
                seen.add(s)
                cleaned.append(s)
        return cleaned
    except FileNotFoundError:
        print(f"[ERRO] Ficheiro não encontrado: {file_path}")
        return []

def build_fqdn(sub: str, base_domain: str) -> str:
    sub = sub.strip().strip(".")
    base_domain = base_domain.strip().strip(".")
    # Se já for FQDN (contém o domínio base no fim), não duplica
    if sub.endswith(base_domain):
        return sub
    return f"{sub}.{base_domain}"

def make_resolver(timeout: float) -> dns.resolver.Resolver:
    r = dns.resolver.Resolver()
    r.timeout = timeout
    r.lifetime = timeout
    return r

def check_subdomain_exists(resolver: dns.resolver.Resolver, fqdn: str) -> tuple[bool, str]:
    """
    Verifica existência via DNS, tentando A, AAAA e CNAME.
    Retorna (existe, tipo_registo_que_validou).
    """
    for rtype in ("A", "AAAA", "CNAME"):
        try:
            resolver.resolve(fqdn, rtype)
            return True, rtype
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
            continue
        except (dns.resolver.NoNameservers, dns.exception.DNSException):
            # erro DNS genérico: consideramos "não validado" e seguimos
            continue
    return False, ""

def save_active_subdomains(file_path: str, subdomains: list[str]) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        for s in subdomains:
            f.write(s + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="Enumeração simples de subdomínios via consultas DNS (uso académico/OSINT)."
    )
    parser.add_argument("--input", "-i", required=True, help="Ficheiro .txt com subdomínios (um por linha).")
    parser.add_argument("--domain", "-d", required=True, help="Domínio base (ex: exemplo.com).")
    parser.add_argument("--output", "-o", default="subdomains_active.txt", help="Ficheiro de saída.")
    parser.add_argument("--timeout", type=float, default=2.0, help="Timeout DNS em segundos.")
    parser.add_argument("--delay", type=float, default=0.1, help="Atraso entre queries (segundos).")
    args = parser.parse_args()

    subs = load_subdomains(args.input)
    if not subs:
        print("[INFO] Nenhum subdomínio carregado.")
        return

    resolver = make_resolver(args.timeout)
    active = []

    print("[INFO] A verificar subdomínios…")
    for sub in subs:
        fqdn = build_fqdn(sub, args.domain)
        exists, rtype = check_subdomain_exists(resolver, fqdn)
        if exists:
            print(f"[VÁLIDO:{rtype}] {fqdn}")
            active.append(fqdn)
        else:
            print(f"[INVÁLIDO] {fqdn}")
        time.sleep(max(0.0, args.delay))

    save_active_subdomains(args.output, active)
    print(f"[OK] Subdomínios ativos guardados em: {args.output}")

if __name__ == "__main__":
    main()
