import argparse


def normalize_domain(d: str) -> str:
    d = d.strip()
    low = d.lower()
    if low.startswith("http://"):
        d = d[7:]
    elif low.startswith("https://"):
        d = d[8:]
    d = d.split("/")[0]
    return d.strip().strip(".").lower()


def normalize_token(s: str) -> str:
    s = s.strip().strip("\"'").strip().strip(".")
    low = s.lower()

    if low.startswith("http://"):
        s = s[7:]
    elif low.startswith("https://"):
        s = s[8:]

    s = s.split("/")[0]

    # remove host:porta simples
    if ":" in s and s.count(":") == 1:
        host, port = s.split(":")
        if port.isdigit():
            s = host

    return s.strip().strip(".").lower()


def clean_wordlist(input_path: str, base_domain: str) -> tuple[list[str], list[str]]:
    base = normalize_domain(base_domain)

    cleaned: list[str] = []
    ignored: list[str] = []
    seen = set()

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue

            tok = normalize_token(line)
            if not tok:
                continue

            # 1) Se for FQDN do alvo -> converte para "sub" relativo
            if tok.endswith("." + base):
                rel = tok[: -(len(base) + 1)]
                if rel and rel not in seen:
                    seen.add(rel)
                    cleaned.append(rel)
                continue

            # 2) Se tiver pontos e NÃO terminar no alvo -> é outro domínio/ruído -> ignora
            # (ex: www.miniclip.com quando alvo é google.com)
            if "." in tok and not tok.endswith("." + base):
                ignored.append(line)
                continue

            # 3) Sub “puro” (www, mail, api, dev, etc.)
            if tok not in seen:
                seen.add(tok)
                cleaned.append(tok)

    return cleaned, ignored


def main():
    p = argparse.ArgumentParser(description="Limpa wordlists 'wild' para enumeração de subdomínios (OSINT).")
    p.add_argument("-i", "--input", required=True, help="Wordlist de entrada.")
    p.add_argument("-d", "--domain", required=True, help="Domínio alvo (ex: exemplo.com).")
    p.add_argument("-o", "--output", default="examples/subdomains_clean.txt", help="Saída (subs limpos).")
    p.add_argument("--ignored", default="examples/ignored_entries.txt", help="Saída (ignorados).")
    args = p.parse_args()

    cleaned, ignored = clean_wordlist(args.input, args.domain)

    with open(args.output, "w", encoding="utf-8") as f:
        for s in cleaned:
            f.write(s + "\n")

    with open(args.ignored, "w", encoding="utf-8") as f:
        for s in ignored:
            f.write(s + "\n")

    print(f"[OK] Clean: {len(cleaned)} -> {args.output}")
    print(f"[OK] Ignored: {len(ignored)} -> {args.ignored}")


if __name__ == "__main__":
    main()
