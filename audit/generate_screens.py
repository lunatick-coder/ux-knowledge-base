"""
Generator makiet wektorowych SVG dla audytu UX platformy ZdrowiePlus.pl
Generuje 5 zrzutów ekranowych (makiet) z naniesionymi anotacjami błędów audytowych.
"""

import os

BASE_DIR = r"C:\Users\Lenovo\.gemini\antigravity\scratch\ux-knowledge-base\audit\screens"
os.makedirs(BASE_DIR, exist_ok=True)

# 1. SCREEN 1: STRONA GŁÓWNA (HOME)
svg_screen_1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 650" width="1000" height="650" style="background:#f8fafc; font-family:'Segoe UI', system-ui, sans-serif;">
  <!-- Browser Chrome / Header Bar -->
  <rect x="0" y="0" width="1000" height="36" fill="#1e293b"/>
  <circle cx="20" cy="18" r="6" fill="#ef4444"/>
  <circle cx="38" cy="18" r="6" fill="#f59e0b"/>
  <circle cx="56" cy="18" r="6" fill="#10b981"/>
  <rect x="120" y="8" width="760" height="20" rx="4" fill="#334155"/>
  <text x="135" y="22" font-size="11" fill="#94a3b8">https://zdrowieplus.pl</text>

  <!-- Top Announcement Bar -->
  <rect x="0" y="36" width="1000" height="30" fill="#0284c7"/>
  <text x="500" y="55" font-size="12" fill="#ffffff" font-weight="600" text-anchor="middle">Darmowa dostawa do aptek i Paczkomatów od 149 zł | Infolinia farmaceutyczna: 800 123 456</text>

  <!-- Main Navigation Header -->
  <rect x="0" y="66" width="1000" height="70" fill="#ffffff" stroke="#e2e8f0"/>
  <!-- Logo -->
  <rect x="40" y="82" width="38" height="38" rx="8" fill="#0284c7"/>
  <text x="59" y="108" font-size="24" fill="#ffffff" font-weight="bold" text-anchor="middle">+</text>
  <text x="90" y="102" font-size="20" fill="#0f172a" font-weight="bold">Zdrowie<tspan fill="#0284c7">Plus</tspan></text>
  <text x="90" y="117" font-size="11" fill="#64748b">Apteka &amp; Sklep Medyczny</text>

  <!-- Search Box Area -->
  <rect x="300" y="81" width="420" height="40" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="316" y="106" font-size="14" fill="#94a3b8">Szukaj leku, ciśnieniomierza, witaminy...</text>
  <rect x="640" y="81" width="80" height="40" rx="6" fill="#0284c7"/>
  <text x="680" y="106" font-size="14" fill="#ffffff" font-weight="600" text-anchor="middle">Szukaj</text>

  <!-- User Utility Icons -->
  <text x="760" y="107" font-size="13" fill="#334155">Infolinia</text>
  <text x="830" y="107" font-size="13" fill="#334155">Moje Konto</text>
  <rect x="910" y="83" width="55" height="36" rx="6" fill="#f1f5f9" stroke="#cbd5e1"/>
  <text x="937" y="106" font-size="14" fill="#0f172a" font-weight="bold" text-anchor="middle">🛒 0</text>

  <!-- Category Nav Bar -->
  <rect x="0" y="136" width="1000" height="40" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="60" y="161" font-size="13" fill="#0284c7" font-weight="bold">Kategorie produktów ▾</text>
  <text x="210" y="161" font-size="13" fill="#334155">Leki bez recepty</text>
  <text x="330" y="161" font-size="13" fill="#334155">Sprzęt medyczny</text>
  <text x="450" y="161" font-size="13" fill="#334155">Witaminy &amp; Minerały</text>
  <text x="590" y="161" font-size="13" fill="#334155">Zdrowie seniora</text>
  <text x="710" y="161" font-size="13" fill="#ef4444" font-weight="600">Promocje %</text>
  <text x="820" y="161" font-size="13" fill="#334155">E-Recepta</text>

  <!-- Hero Section -->
  <rect x="40" y="196" width="920" height="230" rx="12" fill="#e0f2fe" stroke="#bae6fd"/>
  <text x="80" y="246" font-size="28" fill="#0369a1" font-weight="bold">Zadbaj o serce swoje i bliskich</text>
  <text x="80" y="278" font-size="16" fill="#334155">Certyfikowane ciśnieniomierze naramienne z 5-letnią gwarancją producenta.</text>
  <text x="80" y="302" font-size="14" fill="#64748b">Tylko w tym tygodniu zasilacz sieciowy gratis do modeli z serii Pro.</text>
  <!-- Hero CTA -->
  <rect x="80" y="330" width="220" height="46" rx="8" fill="#0284c7"/>
  <text x="190" y="358" font-size="15" fill="#ffffff" font-weight="bold" text-anchor="middle">Sprawdź ciśnieniomierze ›</text>

  <!-- Promo graphic placeholder in Hero -->
  <rect x="680" y="216" width="240" height="190" rx="8" fill="#bae6fd"/>
  <text x="800" y="315" font-size="14" fill="#0284c7" text-anchor="middle">[Grafika Ciśnieniomierza]</text>

  <!-- Popular Categories Section -->
  <text x="40" y="465" font-size="20" fill="#0f172a" font-weight="bold">Najczęściej wybierane kategorie</text>
  
  <!-- Category Cards -->
  <rect x="40" y="485" width="210" height="110" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="145" y="535" font-size="14" fill="#0f172a" font-weight="600" text-anchor="middle">Ciśnieniomierze</text>
  <text x="145" y="555" font-size="12" fill="#64748b" text-anchor="middle">38 produktów</text>

  <rect x="275" y="485" width="210" height="110" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="380" y="535" font-size="14" fill="#0f172a" font-weight="600" text-anchor="middle">Witaminy dla seniora</text>
  <text x="380" y="555" font-size="12" fill="#64748b" text-anchor="middle">64 produkty</text>

  <rect x="510" y="485" width="210" height="110" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="615" y="535" font-size="14" fill="#0f172a" font-weight="600" text-anchor="middle">Inhalatory &amp; Nebulizatory</text>
  <text x="615" y="555" font-size="12" fill="#64748b" text-anchor="middle">22 produkty</text>

  <rect x="745" y="485" width="210" height="110" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="850" y="535" font-size="14" fill="#0f172a" font-weight="600" text-anchor="middle">Glukometry &amp; Paski</text>
  <text x="850" y="555" font-size="12" fill="#64748b" text-anchor="middle">19 produktów</text>

  <!-- === AUDIT ANNOTATIONS === -->
  <!-- Annotation 1: Search Box Placeholder & Contrast -->
  <rect x="295" y="75" width="430" height="52" rx="4" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/>
  <rect x="670" y="50" width="130" height="24" rx="4" fill="#ef4444"/>
  <text x="735" y="66" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">#ERR-01 [CRITICAL]</text>
  <line x1="680" y1="74" x2="650" y2="85" stroke="#ef4444" stroke-width="2"/>

  <!-- Annotation 2: Missing Focus Visible on Nav Links -->
  <rect x="205" y="145" width="450" height="28" rx="4" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
  <rect x="420" y="175" width="120" height="24" rx="4" fill="#f59e0b"/>
  <text x="480" y="191" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">#ERR-02 [MAJOR]</text>
</svg>"""

with open(os.path.join(BASE_DIR, "screen-1-home.svg"), "w", encoding="utf-8") as f:
    f.write(svg_screen_1)

# 2. SCREEN 2: WYNIKI WYSZUKIWANIA I FILTRY
svg_screen_2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 680" width="1000" height="680" style="background:#f8fafc; font-family:'Segoe UI', system-ui, sans-serif;">
  <!-- Browser Chrome -->
  <rect x="0" y="0" width="1000" height="36" fill="#1e293b"/>
  <circle cx="20" cy="18" r="6" fill="#ef4444"/>
  <circle cx="38" cy="18" r="6" fill="#f59e0b"/>
  <circle cx="56" cy="18" r="6" fill="#10b981"/>
  <rect x="120" y="8" width="760" height="20" rx="4" fill="#334155"/>
  <text x="135" y="22" font-size="11" fill="#94a3b8">https://zdrowieplus.pl/szukaj?q=cisnieniomierz</text>

  <!-- Header -->
  <rect x="0" y="36" width="1000" height="65" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="40" y="48" width="34" height="34" rx="6" fill="#0284c7"/>
  <text x="57" y="71" font-size="20" fill="#ffffff" font-weight="bold" text-anchor="middle">+</text>
  <text x="82" y="68" font-size="18" fill="#0f172a" font-weight="bold">Zdrowie<tspan fill="#0284c7">Plus</tspan></text>
  <!-- Search filled -->
  <rect x="250" y="48" width="450" height="38" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
  <text x="265" y="72" font-size="14" fill="#0f172a">cisnieniomiez naramienny</text>
  <rect x="630" y="48" width="70" height="38" rx="6" fill="#0284c7"/>
  <text x="665" y="72" font-size="13" fill="#ffffff" font-weight="600" text-anchor="middle">Szukaj</text>
  <text x="910" y="72" font-size="14" fill="#0f172a" font-weight="bold">🛒 0</text>

  <!-- Breadcrumbs Bar -->
  <rect x="0" y="101" width="1000" height="36" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="40" y="124" font-size="12" fill="#64748b">Strona główna  ›  Sprzęt medyczny  ›  <tspan fill="#0f172a" font-weight="600">Ciśnieniomierze</tspan></text>

  <!-- Main Content Layout -->
  <!-- Left Sidebar (Filters) -->
  <rect x="40" y="150" width="230" height="500" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="60" y="180" font-size="16" fill="#0f172a" font-weight="bold">Filtry (2)</text>
  <text x="210" y="180" font-size="12" fill="#0284c7">Wyczyść</text>

  <!-- Filter Group 1: Typ -->
  <text x="60" y="215" font-size="13" fill="#0f172a" font-weight="600">Typ aparatu</text>
  <!-- Checkbox active -->
  <rect x="60" y="230" width="18" height="18" rx="3" fill="#0284c7"/>
  <text x="69" y="244" font-size="12" fill="#ffffff" text-anchor="middle">✓</text>
  <text x="86" y="244" font-size="13" fill="#0f172a">Naramienny (28)</text>

  <!-- Checkbox inactive -->
  <rect x="60" y="258" width="18" height="18" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="86" y="272" font-size="13" fill="#475569">Nadgarstkowy (10)</text>

  <!-- Filter Group 2: Producent -->
  <line x1="60" y1="290" x2="250" y2="290" stroke="#e2e8f0"/>
  <text x="60" y="315" font-size="13" fill="#0f172a" font-weight="600">Producent</text>
  <!-- Checkbox active -->
  <rect x="60" y="330" width="18" height="18" rx="3" fill="#0284c7"/>
  <text x="69" y="344" font-size="12" fill="#ffffff" text-anchor="middle">✓</text>
  <text x="86" y="344" font-size="13" fill="#0f172a">Omron (12)</text>
  <!-- Inactive -->
  <rect x="60" y="358" width="18" height="18" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="86" y="372" font-size="13" fill="#475569">Microlife (8)</text>
  <rect x="60" y="386" width="18" height="18" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="86" y="400" font-size="13" fill="#475569">Tech-Med (5)</text>

  <!-- Right Content: Listing Title and Chips -->
  <text x="290" y="180" font-size="20" fill="#0f172a" font-weight="bold">Ciśnieniomierze naramienne Omron <tspan font-size="14" fill="#64748b" font-weight="normal">(12 wyników)</tspan></text>
  <!-- Active Filter Chips -->
  <rect x="290" y="195" width="110" height="28" rx="14" fill="#e0f2fe" stroke="#bae6fd"/>
  <text x="302" y="214" font-size="12" fill="#0369a1">Naramienny ✕</text>
  <rect x="410" y="195" width="85" height="28" rx="14" fill="#e0f2fe" stroke="#bae6fd"/>
  <text x="422" y="214" font-size="12" fill="#0369a1">Omron ✕</text>

  <!-- Product Card 1 (Target product) -->
  <rect x="290" y="240" width="670" height="170" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <!-- Image placeholder -->
  <rect x="305" y="255" width="140" height="140" rx="6" fill="#f1f5f9"/>
  <text x="375" y="330" font-size="12" fill="#94a3b8" text-anchor="middle">[Foto: Omron M3]</text>
  
  <text x="465" y="275" font-size="17" fill="#0284c7" font-weight="bold">Omron M3 Comfort Automatyczny Ciśnieniomierz Naramienny</text>
  <text x="465" y="298" font-size="12" fill="#16a34a" font-weight="600">● W magazynie apteki (wysyłka dzisiaj)</text>
  <text x="465" y="325" font-size="13" fill="#475569">Mankiet Intelli Wrap 360° (22-42 cm), wykrywanie arytmii, pamięć 2x60 pomiarów.</text>
  <text x="465" y="345" font-size="12" fill="#64748b">Zasilacz sieciowy w zestawie • 5 lat gwarancji</text>
  
  <!-- Pricing -->
  <text x="465" y="388" font-size="22" fill="#0f172a" font-weight="bold">249,00 zł</text>
  <text x="570" y="388" font-size="11" fill="#94a3b8">Najniższa cena z 30 dni: 249,00 zł</text>

  <!-- CTA -->
  <rect x="800" y="355" width="145" height="42" rx="6" fill="#0284c7"/>
  <text x="872" y="381" font-size="14" fill="#ffffff" font-weight="bold" text-anchor="middle">Do koszyka 🛒</text>

  <!-- Product Card 2 -->
  <rect x="290" y="425" width="670" height="170" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="305" y="440" width="140" height="140" rx="6" fill="#f1f5f9"/>
  <text x="375" y="515" font-size="12" fill="#94a3b8" text-anchor="middle">[Foto: Omron M2]</text>
  <text x="465" y="460" font-size="17" fill="#0284c7" font-weight="bold">Omron M2 Basic Ciśnieniomierz Naramienny z Mankietem 22-32 cm</text>
  <text x="465" y="483" font-size="12" fill="#16a34a" font-weight="600">● W magazynie apteki</text>
  <text x="465" y="510" font-size="13" fill="#475569">Prosta obsługa jednym przyciskiem, walidacja kliniczna.</text>
  <text x="465" y="573" font-size="22" fill="#0f172a" font-weight="bold">169,00 zł</text>
  <rect x="800" y="540" width="145" height="42" rx="6" fill="#0284c7"/>
  <text x="872" y="566" font-size="14" fill="#ffffff" font-weight="bold" text-anchor="middle">Do koszyka 🛒</text>

  <!-- === AUDIT ANNOTATIONS === -->
  <!-- Annotation 3: Checkbox Touch Target Size 18px (WCAG 2.5.8 violation) -->
  <rect x="52" y="222" width="190" height="60" rx="4" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/>
  <rect x="210" y="250" width="130" height="24" rx="4" fill="#ef4444"/>
  <text x="275" y="266" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">#ERR-03 [BLOCKER]</text>

  <!-- Annotation 4: Gray text contrast 2.8:1 on Omnibus disclaimer -->
  <rect x="565" y="374" width="215" height="20" rx="4" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
  <rect x="680" y="398" width="120" height="24" rx="4" fill="#f59e0b"/>
  <text x="740" y="414" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">#ERR-04 [MAJOR]</text>
</svg>"""

with open(os.path.join(BASE_DIR, "screen-2-search-results.svg"), "w", encoding="utf-8") as f:
    f.write(svg_screen_2)

# 3. SCREEN 3: KARTA PRODUKTU (PDP)
svg_screen_3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700" width="1000" height="700" style="background:#f8fafc; font-family:'Segoe UI', system-ui, sans-serif;">
  <!-- Browser Chrome -->
  <rect x="0" y="0" width="1000" height="36" fill="#1e293b"/>
  <circle cx="20" cy="18" r="6" fill="#ef4444"/>
  <circle cx="38" cy="18" r="6" fill="#f59e0b"/>
  <circle cx="56" cy="18" r="6" fill="#10b981"/>
  <rect x="120" y="8" width="760" height="20" rx="4" fill="#334155"/>
  <text x="135" y="22" font-size="11" fill="#94a3b8">https://zdrowieplus.pl/produkt/omron-m3-comfort</text>

  <!-- Header -->
  <rect x="0" y="36" width="1000" height="65" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="40" y="48" width="34" height="34" rx="6" fill="#0284c7"/>
  <text x="57" y="71" font-size="20" fill="#ffffff" font-weight="bold" text-anchor="middle">+</text>
  <text x="82" y="68" font-size="18" fill="#0f172a" font-weight="bold">Zdrowie<tspan fill="#0284c7">Plus</tspan></text>
  <text x="910" y="72" font-size="14" fill="#0f172a" font-weight="bold">🛒 0</text>

  <!-- Breadcrumbs -->
  <text x="40" y="125" font-size="12" fill="#64748b">Strona główna › Sprzęt medyczny › Ciśnieniomierze › <tspan fill="#0f172a" font-weight="600">Omron M3 Comfort</tspan></text>

  <!-- Main Product Grid -->
  <!-- Left: Gallery -->
  <rect x="40" y="145" width="420" height="420" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="60" y="165" width="380" height="300" rx="6" fill="#f1f5f9"/>
  <text x="250" y="325" font-size="16" fill="#94a3b8" text-anchor="middle">[Główne Zdjęcie: Omron M3 + Mankiet + Zasilacz]</text>
  
  <!-- Thumbnails -->
  <rect x="60" y="485" width="70" height="60" rx="4" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
  <text x="95" y="520" font-size="10" fill="#0284c7" text-anchor="middle">Foto 1</text>
  <rect x="145" y="485" width="70" height="60" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="180" y="520" font-size="10" fill="#64748b" text-anchor="middle">Foto 2</text>
  <rect x="230" y="485" width="70" height="60" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="265" y="520" font-size="10" fill="#64748b" text-anchor="middle">Zasilacz</text>

  <!-- Right: Details & Purchase Box -->
  <rect x="480" y="145" width="480" height="490" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  
  <text x="510" y="180" font-size="22" fill="#0f172a" font-weight="bold">Omron M3 Comfort</text>
  <text x="510" y="202" font-size="14" fill="#64748b">Automatyczny ciśnieniomierz naramienny z mankietem Intelli Wrap</text>
  <text x="510" y="224" font-size="13" fill="#f59e0b">★★★★★ <tspan fill="#64748b">(142 opinie z potwierdzeniem zakupu)</tspan></text>

  <!-- Price Box -->
  <rect x="510" y="245" width="420" height="85" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="530" y="280" font-size="28" fill="#0f172a" font-weight="bold">249,00 zł</text>
  <text x="660" y="280" font-size="14" fill="#94a3b8" text-decoration="line-through">289,00 zł</text>
  <text x="530" y="310" font-size="12" fill="#0284c7" font-weight="600">Najniższa cena z 30 dni przed obniżką: 249,00 zł</text>

  <!-- Trust badges -->
  <text x="510" y="355" font-size="13" fill="#16a34a" font-weight="600">✓ W magazynie - wysyłka dzisiaj</text>
  <text x="510" y="375" font-size="13" fill="#475569">✓ Darmowa dostawa do Paczkomatu i kurierem</text>
  <text x="510" y="395" font-size="13" fill="#475569">✓ Oficjalna polska dystrybucja • 5 lat gwarancji</text>

  <!-- Key Specs Box -->
  <rect x="510" y="415" width="420" height="85" rx="6" fill="#f1f5f9"/>
  <text x="525" y="438" font-size="12" fill="#0f172a" font-weight="bold">Co zawiera zestaw:</text>
  <text x="525" y="458" font-size="12" fill="#334155">• Ciśnieniomierz Omron M3 Comfort z pamięcią 2x60</text>
  <text x="525" y="475" font-size="12" fill="#334155">• Mankiet Intelli Wrap (22-42 cm), zasilacz sieciowy, komplet baterii, etui</text>

  <!-- Quantity Selector and Big CTA -->
  <rect x="510" y="525" width="100" height="48" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="530" y="555" font-size="18" fill="#0f172a" font-weight="bold">-</text>
  <text x="560" y="555" font-size="16" fill="#0f172a" font-weight="bold">1</text>
  <text x="590" y="555" font-size="18" fill="#0f172a" font-weight="bold">+</text>

  <rect x="625" y="525" width="305" height="48" rx="8" fill="#16a34a"/>
  <text x="777" y="555" font-size="16" fill="#ffffff" font-weight="bold" text-anchor="middle">Dodaj do koszyka 🛒</text>

  <!-- === AUDIT ANNOTATIONS === -->
  <!-- Annotation 5: Missing Alt tag on thumbnails -->
  <rect x="50" y="475" width="260" height="80" rx="4" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/>
  <rect x="50" y="565" width="130" height="24" rx="4" fill="#ef4444"/>
  <text x="115" y="581" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">#ERR-05 [CRITICAL]</text>
  
  <!-- Annotation 6: Small font in Specs (12px) -->
  <rect x="500" y="405" width="440" height="100" rx="4" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
  <rect x="790" y="390" width="120" height="24" rx="4" fill="#f59e0b"/>
  <text x="850" y="406" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">#ERR-06 [MAJOR]</text>
</svg>"""

with open(os.path.join(BASE_DIR, "screen-3-product-card.svg"), "w", encoding="utf-8") as f:
    f.write(svg_screen_3)

# 4. SCREEN 4: KOSZYK (CART)
svg_screen_4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 680" width="1000" height="680" style="background:#f8fafc; font-family:'Segoe UI', system-ui, sans-serif;">
  <!-- Browser Chrome -->
  <rect x="0" y="0" width="1000" height="36" fill="#1e293b"/>
  <circle cx="20" cy="18" r="6" fill="#ef4444"/>
  <circle cx="38" cy="18" r="6" fill="#f59e0b"/>
  <circle cx="56" cy="18" r="6" fill="#10b981"/>
  <rect x="120" y="8" width="760" height="20" rx="4" fill="#334155"/>
  <text x="135" y="22" font-size="11" fill="#94a3b8">https://zdrowieplus.pl/koszyk</text>

  <!-- Header -->
  <rect x="0" y="36" width="1000" height="65" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="40" y="48" width="34" height="34" rx="6" fill="#0284c7"/>
  <text x="57" y="71" font-size="20" fill="#ffffff" font-weight="bold" text-anchor="middle">+</text>
  <text x="82" y="68" font-size="18" fill="#0f172a" font-weight="bold">Zdrowie<tspan fill="#0284c7">Plus</tspan></text>
  <text x="500" y="72" font-size="16" fill="#0f172a" font-weight="bold" text-anchor="middle">Twój Koszyk Zakupowy (1)</text>

  <!-- Main Grid -->
  <!-- Left: Cart Items -->
  <rect x="40" y="125" width="580" height="210" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  
  <!-- Item 1: Omron M3 -->
  <rect x="60" y="145" width="90" height="90" rx="6" fill="#f1f5f9"/>
  <text x="105" y="195" font-size="11" fill="#94a3b8" text-anchor="middle">[Foto M3]</text>

  <text x="170" y="165" font-size="16" fill="#0f172a" font-weight="bold">Omron M3 Comfort Ciśnieniomierz</text>
  <text x="170" y="185" font-size="12" fill="#64748b">Zasilacz w zestawie • Mankiet 22-42 cm</text>
  <text x="170" y="215" font-size="18" fill="#0f172a" font-weight="bold">249,00 zł</text>

  <!-- Quantity -->
  <rect x="360" y="190" width="80" height="34" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="375" y="212" font-size="14" fill="#0f172a">-</text>
  <text x="400" y="212" font-size="14" fill="#0f172a" font-weight="bold">1</text>
  <text x="425" y="212" font-size="14" fill="#0f172a">+</text>
  
  <text x="540" y="212" font-size="13" fill="#ef4444" text-anchor="middle">Usuń ✕</text>

  <!-- DARK PATTERN ITEM: SNEAK INTO BASKET TRAP -->
  <rect x="60" y="250" width="540" height="65" rx="6" fill="#fef2f2" stroke="#fecaca"/>
  <rect x="75" y="272" width="18" height="18" rx="3" fill="#ef4444"/>
  <text x="84" y="286" font-size="12" fill="#ffffff" text-anchor="middle">✓</text>
  <text x="105" y="280" font-size="13" fill="#991b1b" font-weight="bold">Ubezpieczenie przesyłki medycznej i ochrona przed uszkodzeniem</text>
  <text x="105" y="298" font-size="11" fill="#7f1d1d">Automatycznie dodano do Twojego koszyka (+6,99 zł)</text>
  <text x="540" y="286" font-size="14" fill="#991b1b" font-weight="bold">+6,99 zł</text>

  <!-- Cross-sell Section: Witamina D3 -->
  <rect x="40" y="355" width="580" height="130" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="60" y="380" font-size="14" fill="#0f172a" font-weight="bold">Dobierz do zamówienia dla seniora:</text>
  <rect x="60" y="395" width="50" height="50" rx="4" fill="#f1f5f9"/>
  <text x="85" y="425" font-size="9" fill="#94a3b8" text-anchor="middle">[D3]</text>
  <text x="125" y="415" font-size="13" fill="#0f172a" font-weight="600">Witamina D3 4000 IU Forte dla seniorów (60 kapsułek)</text>
  <text x="125" y="435" font-size="14" fill="#0284c7" font-weight="bold">24,90 zł</text>
  <rect x="480" y="405" width="120" height="34" rx="6" fill="#e0f2fe" stroke="#0284c7"/>
  <text x="540" y="427" font-size="12" fill="#0284c7" font-weight="bold" text-anchor="middle">+ Dodaj do koszyka</text>

  <!-- Right: Order Summary Box -->
  <rect x="640" y="125" width="320" height="360" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="665" y="160" font-size="18" fill="#0f172a" font-weight="bold">Podsumowanie</text>
  
  <text x="665" y="195" font-size="13" fill="#475569">Wartość produktów:</text>
  <text x="935" y="195" font-size="13" fill="#0f172a" font-weight="bold" text-anchor="end">249,00 zł</text>

  <text x="665" y="225" font-size="13" fill="#475569">Ubezpieczenie przesyłki:</text>
  <text x="935" y="225" font-size="13" fill="#0f172a" font-weight="bold" text-anchor="end">6,99 zł</text>

  <text x="665" y="255" font-size="13" fill="#475569">Dostawa (Paczkomat InPost):</text>
  <text x="935" y="255" font-size="13" fill="#16a34a" font-weight="bold" text-anchor="end">0,00 zł (Darmowa)</text>

  <line x1="665" y1="280" x2="935" y2="280" stroke="#e2e8f0"/>
  <text x="665" y="310" font-size="15" fill="#0f172a" font-weight="bold">Do zapłaty:</text>
  <text x="935" y="310" font-size="22" fill="#0284c7" font-weight="bold" text-anchor="end">255,99 zł</text>

  <!-- Big Checkout CTA -->
  <rect x="665" y="340" width="270" height="48" rx="8" fill="#0284c7"/>
  <text x="800" y="370" font-size="16" fill="#ffffff" font-weight="bold" text-anchor="middle">Przejdź do kasy ›</text>
  
  <text x="800" y="420" font-size="12" fill="#64748b" text-anchor="middle">🔒 Bezpieczne zakupy z certyfikatem SSL</text>

  <!-- === AUDIT ANNOTATIONS === -->
  <!-- Annotation 7: Sneak into basket (Dark Pattern BLOCKER) -->
  <rect x="50" y="240" width="560" height="85" rx="6" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4"/>
  <rect x="360" y="228" width="140" height="24" rx="4" fill="#ef4444"/>
  <text x="430" y="244" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">#ERR-07 [BLOCKER]</text>

  <!-- Annotation 8: Small delete link target (Fitts Law violation) -->
  <rect x="510" y="195" width="60" height="26" rx="4" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
  <rect x="520" y="168" width="120" height="24" rx="4" fill="#f59e0b"/>
  <text x="580" y="184" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">#ERR-08 [MAJOR]</text>
</svg>"""

with open(os.path.join(BASE_DIR, "screen-4-cart.svg"), "w", encoding="utf-8") as f:
    f.write(svg_screen_4)

# 5. SCREEN 5: CHECKOUT (KASA I FORMULARZ)
svg_screen_5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 740" width="1000" height="740" style="background:#f8fafc; font-family:'Segoe UI', system-ui, sans-serif;">
  <!-- Browser Chrome -->
  <rect x="0" y="0" width="1000" height="36" fill="#1e293b"/>
  <circle cx="20" cy="18" r="6" fill="#ef4444"/>
  <circle cx="38" cy="18" r="6" fill="#f59e0b"/>
  <circle cx="56" cy="18" r="6" fill="#10b981"/>
  <rect x="120" y="8" width="760" height="20" rx="4" fill="#334155"/>
  <text x="135" y="22" font-size="11" fill="#94a3b8">https://zdrowieplus.pl/zamowienie/kasa</text>

  <!-- Header minimal (Distraction-free checkout) -->
  <rect x="0" y="36" width="1000" height="60" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="50" y="72" font-size="18" fill="#0f172a" font-weight="bold">Zdrowie<tspan fill="#0284c7">Plus</tspan> | Kasa</text>
  <text x="910" y="72" font-size="13" fill="#16a34a" font-weight="600">🔒 Bezpieczne połączenie</text>

  <!-- Progress Steps -->
  <rect x="0" y="96" width="1000" height="40" fill="#f1f5f9"/>
  <text x="250" y="121" font-size="13" fill="#16a34a" font-weight="bold">✓ 1. Koszyk</text>
  <text x="450" y="121" font-size="13" fill="#0284c7" font-weight="bold">● 2. Dostawa i dane</text>
  <text x="680" y="121" font-size="13" fill="#94a3b8">○ 3. Płatność i potwierdzenie</text>

  <!-- Main Checkout Grid -->
  <!-- Left: Single Column Form -->
  <rect x="40" y="150" width="580" height="560" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="70" y="185" font-size="18" fill="#0f172a" font-weight="bold">Dane do wysyłki (Zakupy bez rejestracji)</text>

  <!-- Field 1: Imię i Nazwisko -->
  <text x="70" y="220" font-size="13" fill="#0f172a" font-weight="600">Imię i nazwisko *</text>
  <rect x="70" y="230" width="520" height="40" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="85" y="255" font-size="14" fill="#0f172a">Teresa Wiśniewska</text>

  <!-- Field 2: E-mail -->
  <text x="70" y="295" font-size="13" fill="#0f172a" font-weight="600">Adres e-mail (do powiadomień) *</text>
  <rect x="70" y="305" width="520" height="40" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="85" y="330" font-size="14" fill="#0f172a">teresa.wisniewska@example.com</text>

  <!-- Field 3: Telefon (WITH ERROR DISPLAY) -->
  <text x="70" y="370" font-size="13" fill="#ef4444" font-weight="600">Numer telefonu komórkowego *</text>
  <rect x="70" y="380" width="520" height="40" rx="6" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
  <text x="85" y="405" font-size="14" fill="#0f172a">60112345</text>
  <!-- Error Text -->
  <text x="70" y="435" font-size="12" fill="#ef4444">⚠️ Nieprawidłowy numer telefonu. Wymagane jest dokładnie 9 cyfr (np. 601 123 456).</text>

  <!-- Delivery Method: Paczkomat -->
  <text x="70" y="475" font-size="15" fill="#0f172a" font-weight="bold">Sposób dostawy:</text>
  <rect x="70" y="490" width="520" height="50" rx="6" fill="#e0f2fe" stroke="#0284c7"/>
  <text x="90" y="520" font-size="14" fill="#0284c7" font-weight="bold">🔘 Paczkomat InPost (RAD04M - ul. Struga 14) - 0,00 zł</text>

  <!-- Consents Checkbox area -->
  <rect x="70" y="560" width="16" height="16" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="95" y="573" font-size="12" fill="#475569">Oświadczam, że zapoznałem się z Regulaminem apteki i akceptuję jego warunki *</text>

  <!-- Big Final CTA -->
  <rect x="70" y="610" width="520" height="52" rx="8" fill="#16a34a"/>
  <text x="330" y="642" font-size="17" fill="#ffffff" font-weight="bold" text-anchor="middle">Kupuję i płacę z BLIK (249,00 zł) ›</text>

  <!-- Right: Sticky Order Summary -->
  <rect x="640" y="150" width="320" height="300" rx="8" fill="#ffffff" stroke="#e2e8f0"/>
  <text x="665" y="185" font-size="16" fill="#0f172a" font-weight="bold">Twoje Zamówienie</text>
  
  <text x="665" y="215" font-size="13" fill="#475569">Omron M3 Comfort (1 szt.)</text>
  <text x="935" y="215" font-size="13" fill="#0f172a" font-weight="bold" text-anchor="end">249,00 zł</text>

  <text x="665" y="245" font-size="13" fill="#475569">Dostawa Paczkomat:</text>
  <text x="935" y="245" font-size="13" fill="#16a34a" font-weight="bold" text-anchor="end">0,00 zł</text>

  <line x1="665" y1="270" x2="935" y2="270" stroke="#e2e8f0"/>
  <text x="665" y="300" font-size="16" fill="#0f172a" font-weight="bold">Łącznie:</text>
  <text x="935" y="300" font-size="22" fill="#0284c7" font-weight="bold" text-anchor="end">249,00 zł</text>

  <rect x="665" y="330" width="270" height="80" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
  <text x="680" y="355" font-size="12" fill="#16a34a" font-weight="bold">✓ Płatność BLIK bez prowizji</text>
  <text x="680" y="375" font-size="11" fill="#64748b">• 14 dni na bezpłatny zwrot</text>
  <text x="680" y="393" font-size="11" fill="#64748b">• Apteka zarejestrowana w WIF</text>

  <!-- === AUDIT ANNOTATIONS === -->
  <!-- Annotation 9: Redundant entry & missing autocomplete attribute -->
  <rect x="60" y="220" width="540" height="150" rx="4" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
  <rect x="420" y="200" width="130" height="24" rx="4" fill="#f59e0b"/>
  <text x="485" y="216" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">#ERR-09 [MAJOR]</text>

  <!-- Annotation 10: Checkbox target size 16px (WCAG 2.5.8 violation) -->
  <rect x="60" y="550" width="530" height="35" rx="4" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/>
  <rect x="440" y="530" width="140" height="24" rx="4" fill="#ef4444"/>
  <text x="510" y="546" font-size="11" fill="#ffffff" font-weight="bold" text-anchor="middle">#ERR-10 [BLOCKER]</text>
</svg>"""

with open(os.path.join(BASE_DIR, "screen-5-checkout.svg"), "w", encoding="utf-8") as f:
    f.write(svg_screen_5)

print("Wygenerowano 5 makiet wektorowych SVG z anotacjami w katalogu:", BASE_DIR)
