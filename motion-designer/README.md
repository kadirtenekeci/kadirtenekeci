# Claude Motion Designer

Claude ile animasyon üretmenin üç yolu, aynı hareket kurallarını (süre/easing token'ları,
reduced-motion, sadece `transform`/`opacity`) paylaşır.

| Parça | Yer | Nasıl kullanılır |
|---|---|---|
| **Skill** | `.claude/skills/motion-designer/` | Claude Code'da "bir loader animasyonu yap" gibi bir istek yeterli; skill otomatik devreye girer. |
| **Subagent** | `.claude/agents/motion-designer.md` | "motion-designer ajanını kullanarak README için animasyonlu SVG banner yap" de. Çıktılar `motion/` klasörüne yazılır. |
| **Web uygulaması** | `motion-designer/index.html` | Dosyayı tarayıcıda aç, API anahtarını gir, isteğini yaz. Önizleme, kod, tekrar oynatma ve indirme içerir. |

## Web uygulaması notları

- Anthropic TypeScript SDK'sını jsdelivr üzerinden yükler; kurulum veya derleme gerekmez.
- API anahtarı yalnızca senin tarayıcında (`localStorage`) tutulur ve doğrudan Anthropic API'sine
  gönderilir. Uygulamayı herkese açık bir yerde yayınlarsan herkes kendi anahtarını girmeli; kendi
  anahtarını gömme.
- Varsayılan model Claude Opus 5.5 (effort `medium`); Claude Sonnet 5.5 daha ucuz bir seçenek.
- İlk sonuçtan sonra düzeltme istekleri aynı sohbette devam eder; "Yeni sohbet" sıfırlar.
- Üretilen kod `sandbox="allow-scripts"` bir iframe içinde çalışır.

## claude.ai sürümü (API anahtarı gerekmez)

`motion-designer/artifact.html`, claude.ai'de Artifact olarak yayınlanan sürümdür. Claude'a
açan kişinin kendi Claude hesabıyla bağlanır, bu yüzden API anahtarı istemez. İlk kullanımda
izin sorar ve kullanım açan kişinin Claude kotasından düşer.
