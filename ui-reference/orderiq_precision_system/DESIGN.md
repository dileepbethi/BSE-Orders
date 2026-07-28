---
name: OrderIQ Precision System
colors:
  surface: '#10131a'
  surface-dim: '#10131a'
  surface-bright: '#363941'
  surface-container-lowest: '#0b0e15'
  surface-container-low: '#191b23'
  surface-container: '#1d2027'
  surface-container-high: '#272a31'
  surface-container-highest: '#32353c'
  on-surface: '#e1e2ec'
  on-surface-variant: '#c2c6d6'
  inverse-surface: '#e1e2ec'
  inverse-on-surface: '#2e3038'
  outline: '#8c909f'
  outline-variant: '#424754'
  surface-tint: '#adc6ff'
  primary: '#adc6ff'
  on-primary: '#002e6a'
  primary-container: '#4d8eff'
  on-primary-container: '#00285d'
  inverse-primary: '#005ac2'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#ffb786'
  on-tertiary: '#502400'
  tertiary-container: '#df7412'
  on-tertiary-container: '#461f00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdcc6'
  tertiary-fixed-dim: '#ffb786'
  on-tertiary-fixed: '#311400'
  on-tertiary-fixed-variant: '#723600'
  background: '#10131a'
  on-background: '#e1e2ec'
  surface-variant: '#32353c'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  title-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 16px
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  container-margin: 24px
  gutter: 16px
---

## Brand & Style
The design system is engineered for high-stakes financial intelligence. It blends the data density of a professional trading terminal with the refined, breathable aesthetics of modern enterprise software. The personality is authoritative, precise, and high-velocity.

The style is **Corporate Modern with a "Glass-Substrate" influence**. It utilizes a dark, layered architecture to maintain focus during extended sessions, using subtle borders and tonal shifts rather than heavy shadows to define hierarchy. Every pixel is optimized for legibility and the rapid scanning of complex Indian market data.

## Colors
The palette is rooted in a "Deep Navy" foundation to reduce eye strain.
- **Surface Strategy:** Backgrounds use `#0F172A`. Sidebars and secondary containers use `#1E293B`. Cards and active elements use a slightly lighter slate to "lift" content.
- **Financial Indicators:** Success (`#10B981`) and Error (`#EF4444`) are calibrated for high accessibility against the dark backdrop.
- **Indian Market Context:** Accent colors should be used sparingly for "Buy/Sell" indicators, ensuring the ₹ symbol always carries the same visual weight as the numerical data.

## Typography
This design system utilizes **Inter** for all UI and prose to maintain a clean, neutral tone. For numerical data, specifically stock prices, quantities, and Indian numbering (Lakhs/Crores), use **JetBrains Mono** to ensure tabular alignment and character clarity.

**Special Handling:** 
- The ₹ symbol should be sized at 90% of the accompanying numerical value to keep the focus on the figure.
- Use `label-caps` for table headers and sidebar category labels to provide clear structural anchoring.

## Layout & Spacing
The system operates on a **strict 8px linear grid**. 
- **Grid System:** A 12-column fluid grid is used for dashboard views. 
- **Density:** In data-heavy views (Order Books, Portfolio Analyzers), padding is reduced to `sm` (8px) to maximize information density. For editorial or report views, use `md` (16px) or `lg` (24px) padding.
- **Sidebar:** A fixed-width left navigation (240px-280px) provides a persistent anchor.

## Elevation & Depth
Depth is communicated through **Tonal Layering** and **Stroke Definition** rather than shadows.
- **Level 0 (Base):** `#0F172A` - Main application background.
- **Level 1 (Surface):** `#1E293B` - Sidebars, headers, and navigation rails.
- **Level 2 (Elevated):** `#1E293B` with a `1px solid #334155` border - Content cards and data tables.
- **Interactions:** Hover states on rows should use a subtle highlight of `#334155` at 50% opacity.

## Shapes
The system uses a **Medium Rounded** aesthetic to soften the technical nature of the data.
- **Standard Radius:** 8px for buttons, input fields, and small cards.
- **Large Radius:** 12px for main container cards and modal overlays.
- **Data Tags:** 4px radius for status chips (e.g., "Executed", "Pending").

## Components
- **Data Tables:** Headers must be high-contrast (`#94A3B8`) with a bottom border of 2px. Rows use a 1px border-bottom. High-density rows (32px height) are the default for market watchlists.
- **Stat Cards:** Feature a "Micro-Chart" (sparkline) in the background. The primary metric (e.g., Portfolio Value) uses `display-lg` typography.
- **Sidebar:** Icons are stroke-based (2px weight). Active states use a vertical 3px "Professional Blue" bar on the left edge.
- **PDF Viewer:** Encapsulated in a `Level 2` surface with a dedicated dark-grey toolbar. The document itself is rendered on a slightly off-white background to simulate physical paper, providing a "focus mode" contrast.
- **Buttons:** Primary buttons use a solid `#3B82F6` fill. Secondary buttons use a "Ghost" style with a `#334155` border and white text.
- **Input Fields:** Dark fills (`#0F172A`) with a subtle 1px border. Focus state triggers a 1px blue glow.