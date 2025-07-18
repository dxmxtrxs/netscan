from scapy.all import IP, TCP, sr1, ICMP

def detect_os(ip):
    try:
        # Try TCP SYN to port 80
        pkt = IP(dst=ip)/TCP(dport=80, flags="S")
        ans = sr1(pkt, timeout=2, verbose=0)
        
        if not ans:
            # Fallback to ICMP
            icmp_pkt = IP(dst=ip)/ICMP()
            ans = sr1(icmp_pkt, timeout=2, verbose=0)

        if ans:
            ttl = int(ans.ttl)
            window = ans.getlayer(TCP).window if ans.haslayer(TCP) else None

            # Rough OS guess based on TTL
            if ttl <= 64:
                os = "Linux/Unix"
            elif ttl <= 128:
                os = "Windows"
            elif ttl <= 255:
                os = "Cisco/Network Device"
            else:
                os = "Unknown"

            return {
                "ip": ip,
                "ttl": ttl,
                "tcp_window": window,
                "os_guess": os
            }
        else:
            return {"ip": ip, "error": "No response from host"}

    except Exception as e:
        return {"ip": ip, "error": str(e)}