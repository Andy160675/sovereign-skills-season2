# Biophilic Luxury Design System

## Table of Contents
1. Design Philosophy
2. Color Palette (OKLCH)
3. Typography
4. Component Classes
5. Page Structure
6. Font Loading
7. Motion & Animation

## 1. Design Philosophy

Luxury biophilic: warm, organic, institutional. NOT hacker terminal, NOT corporate SaaS.
Think private members' club, not startup dashboard. Matte surfaces, paper-like depth, subtle grain.

Key principles:
- Warm stone backgrounds, not white or dark
- Forest green primary, gold accents — not blue
- Serif headings (Cormorant Garamond) for authority
- Monospace ONLY for audit/hash data
- Slow intentional motion (400-600ms)
- Organic icons, leaf/branch motifs for empty states

## 2. Color Palette (OKLCH for Tailwind 4)

```css
@theme inline {
  --color-background: oklch(0.97 0.005 80);       /* warm stone */
  --color-foreground: oklch(0.20 0.01 60);         /* charcoal */
  --color-card: oklch(0.98 0.004 80);              /* cream surface */
  --color-primary: oklch(0.35 0.08 145);           /* forest green */
  --color-primary-foreground: oklch(0.97 0.005 80);
  --color-secondary: oklch(0.92 0.008 80);         /* light stone */
  --color-accent: oklch(0.70 0.10 85);             /* warm gold */
  --color-muted: oklch(0.93 0.006 80);
  --color-muted-foreground: oklch(0.50 0.02 60);
  --color-border: oklch(0.88 0.012 80);
  --color-destructive: oklch(0.55 0.15 25);        /* muted red */
}
```

## 3. Typography

| Role | Font | Weight | Usage |
|------|------|--------|-------|
| Display/Headings | Cormorant Garamond | 500-700 | h1-h6, page titles, hero text |
| Body | Source Sans 3 | 300-700 | Paragraphs, labels, UI text |
| Audit/Code | JetBrains Mono | 400-600 | Hashes, audit entries, code |

Load via Google Fonts in `index.html`:
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Source+Sans+3:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

CSS font stacks:
```css
--font-sans: 'Source Sans 3', ui-sans-serif, system-ui, sans-serif;
--font-serif: 'Cormorant Garamond', ui-serif, Georgia, serif;
--font-mono: 'JetBrains Mono', ui-monospace, monospace;
```

Apply serif to all headings:
```css
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-serif);
  font-weight: 600;
  letter-spacing: -0.01em;
}
```

## 4. Component Classes

```css
/* Sovereign surface cards */
.sovereign-surface {
  background: var(--color-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: 0 1px 3px 0 oklch(0 0 0 / 0.04);
}

.sovereign-surface-elevated {
  box-shadow: 0 4px 6px -1px oklch(0 0 0 / 0.06);
}

/* Grain texture overlay */
.grain-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  opacity: 0.025;
  background-image: url("data:image/svg+xml,..."); /* noise SVG */
  pointer-events: none;
}
```

## 5. Page Structure

Every page uses: `<PageLayout>` → `<Navigation />` + content + `<Footer />`

Navigation: top bar with logo, nav links (Boardroom, Constitution, Decisions, Audit Chain, Extensions), settings gear, user profile.

NOT a sidebar layout — this is a public-facing governance platform.

## 6. Font Loading

Add `<link rel="preconnect">` for Google Fonts in `client/index.html` head.

## 7. Motion & Animation

- Transitions: 400-600ms with `cubic-bezier(0.4, 0, 0.2, 1)`
- Vote badge pulse: subtle scale animation on new votes
- Agent processing: sequential reveal with staggered delays
- Page transitions: fade-in on mount
- Avoid: bounce, shake, or attention-grabbing animations
