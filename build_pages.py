import os

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Global variables
brand_name = "Pierce Law"
lawyer_name = "Alexander Pierce, Esq."
tagline = "Relentless Advocacy. Proven Results."

# Header
header = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{brand_name} - {tagline}">
  <title>{brand_name} | {lawyer_name}</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <style>
    /* Lawyer specific CSS overrides */
    h1, h2, h3, h4, .section-title, .hero-title, .logo-text {{
      font-family: 'Playfair Display', serif;
    }}
    .hero-title span.gradient-text {{
      background: linear-gradient(90deg, #d4af37, #f3e5ab);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .btn-primary {{
      background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
    }}
    .btn-primary:hover {{
      box-shadow: 0 8px 25px rgba(30, 60, 114, 0.4);
    }}
  </style>
</head>
<body>
  <!-- --- HEADER --- -->
  <header class="header">
    <div class="container header-container">
      <a href="index.html" class="logo">
        <div style="width: 45px; height: 45px; border-radius: 8px; background: linear-gradient(135deg, var(--color-primary), var(--bg-tertiary)); border: 1px solid rgba(212, 175, 55, 0.5); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
          <span style="font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 700; background: linear-gradient(90deg, #d4af37, #f3e5ab); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1;">P</span>
        </div>
        <div class="logo-text">Pierce<span>Law</span></div>
      </a>
      
      <button class="mobile-toggle" id="mobile-toggle" aria-label="Toggle Menu">
        <span></span>
        <span></span>
        <span></span>
      </button>

      <nav class="nav" aria-label="Main Navigation">
        <ul class="nav-menu">
          <li><a href="about-attorney.html" class="nav-link">About Alexander</a></li>
          <li class="nav-item-dropdown">
            <a href="practice-areas.html" class="nav-link">Practice Areas <svg style="width: 10px; height: 10px; margin-left: 4px; fill: currentColor; display: inline-block;" viewBox="0 0 320 512"><path d="M143 352.3L7 216.3c-9.4-9.4-9.4-24.6 0-33.9l22.6-22.6c9.4-9.4 24.6-9.4 33.9 0l96.4 96.4 96.4-96.4c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9l-136 136c-9.2 9.4-24.4 9.4-33.8 0z"/></svg></a>
            <ul class="dropdown-menu">
              <li><a href="practice-areas.html#corporate" class="dropdown-link">Corporate Law</a></li>
              <li><a href="practice-areas.html#litigation" class="dropdown-link">Litigation</a></li>
              <li><a href="practice-areas.html#ip" class="dropdown-link">Intellectual Property</a></li>
            </ul>
          </li>
          <li><a href="case-results.html" class="nav-link">Case Results</a></li>
          <li><a href="legal-blog.html" class="nav-link">Legal Insights</a></li>
        </ul>
      </nav>

      <div class="header-actions">
        <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Dark Mode">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22ZM12 20V4C16.4183 4 20 7.58172 20 12C20 16.4183 16.4183 20 12 20Z"></path>
          </svg>
        </button>
        <a href="consultation.html" class="btn btn-primary btn-sm">Free Consultation</a>
      </div>
    </div>
  </header>
"""

# Hero Section
hero = f"""
  <!-- --- HERO SECTION --- -->
  <section class="hero" id="hero" style="padding: 120px 0 80px 0; min-height: 85vh; display: flex; align-items: center;">
    <div class="container hero-container grid">
      <div class="hero-content" style="padding-right: 2rem;">
        <h1 class="hero-title" style="font-size: 3.5rem; line-height: 1.1; margin-bottom: 1.5rem;">{tagline} <br><span class="gradient-text">{lawyer_name}</span></h1>
        <div style="width: 60px; height: 3px; background: var(--color-accent); margin-bottom: 1.5rem;"></div>
        <p class="hero-subtitle" style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 2.5rem; max-width: 90%;">Specializing in high-stakes corporate litigation and intellectual property disputes. We do not just take cases; we take on causes. When your future is on the line, you need Pierce Law.</p>
        <div class="hero-cta flex-wrap" style="display: flex; gap: 1rem; margin-bottom: 3rem;">
          <a href="consultation.html" class="btn btn-primary" style="padding: 1rem 2rem; font-size: 1.1rem;">Evaluate My Case</a>
          <a href="case-results.html" class="btn btn-secondary" style="padding: 1rem 2rem; font-size: 1.1rem; border-color: rgba(212,175,55,0.3); color: var(--text-primary);">View Case Results</a>
        </div>
      </div>

      <div class="hero-visual" style="position: relative;">
        <!-- Elegant Frame -->
        <div style="position: absolute; top: -15px; left: 15px; width: 100%; height: 100%; border: 2px solid var(--color-accent); border-radius: var(--border-radius-md); z-index: 1;"></div>
        
        <img class="hero-image" src="images/lawyer_hero_1779391732649.png" alt="Alexander Pierce, Esq." style="width:100%; border-radius:var(--border-radius-md); box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); position:relative; z-index:2; display: block;">
      </div>
    </div>
  </section>
"""

# Stats Section
stats = """
  <!-- --- STATS SECTION --- -->
  <section class="stats section-padding reveal bg-tertiary">
    <div class="container">
      <div class="stats-grid grid">
        <div class="stat-card">
          <h3 class="stat-number gradient-text" data-target="25" data-suffix="+">0+</h3>
          <p class="stat-label">Years of Experience</p>
        </div>
        <div class="stat-card">
          <h3 class="stat-number gradient-text" data-target="50" data-suffix="M+">0M+</h3>
          <p class="stat-label">Dollars Recovered</p>
        </div>
        <div class="stat-card">
          <h3 class="stat-number gradient-text" data-target="150" data-suffix="+">0+</h3>
          <p class="stat-label">Cases Won at Trial</p>
        </div>
        <div class="stat-card">
          <h3 class="stat-number gradient-text" data-target="100" data-suffix="%">0%</h3>
          <p class="stat-label">Confidentiality Assured</p>
        </div>
      </div>
    </div>
  </section>
"""

# Practice Areas
practice_areas = """
  <!-- --- PRACTICE AREAS SECTION --- -->
  <section class="values section-padding reveal" id="practice-areas">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-badge" style="background: rgba(212,175,55,0.1); color: var(--color-accent); border: 1px solid var(--color-accent);">Our Expertise</span>
        <h2 class="section-title">Practice Areas</h2>
        <p class="section-subtitle">We provide elite legal representation in complex litigation and corporate matters.</p>
      </div>
      
      <style>
        .luxury-card {
          position: relative;
          height: 450px;
          border-radius: 12px;
          overflow: hidden;
          cursor: pointer;
          border: 1px solid rgba(212, 175, 55, 0.2);
          box-shadow: 0 10px 30px rgba(0,0,0,0.5);
          transition: all 0.4s ease;
        }
        .luxury-card:hover {
          transform: translateY(-10px);
          border: 1px solid rgba(212, 175, 55, 0.6);
          box-shadow: 0 20px 40px rgba(212, 175, 55, 0.15);
        }
        .luxury-card img {
          position: absolute;
          top: 0; left: 0;
          width: 100%; height: 100%;
          object-fit: cover;
          transition: transform 0.6s ease;
        }
        .luxury-card:hover img {
          transform: scale(1.08);
        }
        .luxury-card .overlay {
          position: absolute;
          bottom: 0; left: 0; width: 100%;
          height: 70%;
          background: linear-gradient(to top, rgba(15, 22, 36, 0.95) 0%, rgba(15, 22, 36, 0.7) 50%, rgba(15, 22, 36, 0) 100%);
          display: flex;
          flex-direction: column;
          justify-content: flex-end;
          padding: 2.5rem 2rem;
          transition: all 0.4s ease;
        }
        .luxury-card h3 {
          font-family: 'Playfair Display', serif;
          font-size: 1.8rem;
          color: white;
          margin-bottom: 0.5rem;
          position: relative;
        }
        .luxury-card h3::after {
          content: '';
          position: absolute;
          bottom: -10px; left: 0;
          width: 40px; height: 2px;
          background: var(--color-accent);
          transition: width 0.4s ease;
        }
        .luxury-card:hover h3::after {
          width: 80px;
        }
        .luxury-card p {
          color: #cbd5e1;
          font-size: 0.95rem;
          margin-top: 1.5rem;
          opacity: 0.8;
          transform: translateY(10px);
          transition: all 0.4s ease;
        }
        .luxury-card:hover p {
          opacity: 1;
          transform: translateY(0);
        }
      </style>

      <div class="values-grid grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 3rem;">
        <!-- Corporate -->
        <div class="luxury-card">
          <img src="images/practice_corporate_1779391756299.png" alt="Corporate Law">
          <div class="overlay">
            <h3>Corporate Law</h3>
            <p>Mergers, acquisitions, compliance, and corporate governance for Fortune 500 companies and high-growth startups.</p>
          </div>
        </div>

        <!-- IP -->
        <div class="luxury-card">
          <img src="images/practice_ip_1779391756916.png" alt="Intellectual Property">
          <div class="overlay">
            <h3>Intellectual Property</h3>
            <p>Protecting your most valuable assets through patent litigation, trademark registration, and trade secret defense.</p>
          </div>
        </div>

        <!-- Litigation -->
        <div class="luxury-card">
          <img src="images/practice_litigation_1779391771467.png" alt="Litigation">
          <div class="overlay">
            <h3>Commercial Litigation</h3>
            <p>Aggressive trial advocacy in breach of contract, partnership disputes, and complex business litigation.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# Case Evaluation Tool (Matcher Replacement)
matcher = """
  <!-- --- CASE EVALUATION WIDGET --- -->
  <section class="matcher section-padding reveal bg-tertiary" id="consultation">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-badge" style="background: rgba(212,175,55,0.1); color: var(--color-accent); border: 1px solid var(--color-accent);">Free Review</span>
        <h2 class="section-title">Interactive Case Evaluation</h2>
        <p class="section-subtitle">Answer a few quick questions to see how Pierce Law can assist with your legal matter.</p>
      </div>
      
      <style>
        .matcher-container {
          max-width: 800px;
          margin: 0 auto;
          background: var(--bg-secondary);
          border: 1px solid rgba(212, 175, 55, 0.3);
          box-shadow: 0 20px 40px rgba(0,0,0,0.2);
          padding: 3rem;
          border-radius: var(--border-radius-lg);
        }
        .step-title {
          font-family: 'Playfair Display', serif;
          font-size: 1.8rem;
          margin-bottom: 2rem;
          text-align: center;
          color: var(--text-primary);
        }
        .options-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
          gap: 1.5rem;
        }
        .matcher-option, .matcher-checkbox {
          padding: 1.5rem;
          border: 2px solid var(--glass-border);
          border-radius: 12px;
          cursor: pointer;
          transition: all 0.3s ease;
          display: flex;
          flex-direction: column;
          align-items: center;
          text-align: center;
          background: var(--bg-primary);
        }
        .matcher-option:hover, .matcher-checkbox:hover {
          border-color: rgba(212, 175, 55, 0.5);
          background: rgba(212, 175, 55, 0.05);
          transform: translateY(-3px);
        }
        .matcher-option.selected, .matcher-checkbox.selected {
          border-color: var(--color-accent);
          background: rgba(212, 175, 55, 0.1);
          box-shadow: 0 10px 20px rgba(212, 175, 55, 0.1);
        }
        .option-icon {
          width: 40px; height: 40px;
          margin-bottom: 1rem;
          color: var(--color-accent);
        }
        .option-title {
          font-weight: 600;
          font-size: 1.1rem;
          color: var(--text-primary);
          margin-bottom: 0.5rem;
        }
        .option-desc {
          font-size: 0.9rem;
          color: var(--text-secondary);
        }
      </style>

      <div class="matcher-container card-glass" id="job-matcher-widget">
        <!-- Progress Bar -->
        <div class="matcher-progress-container" style="background: rgba(255,255,255,0.1); height: 6px; border-radius: 3px; margin-bottom: 2.5rem; overflow: hidden;">
          <div class="matcher-progress" style="width: 33.33%; height: 100%; background: var(--color-accent); transition: width 0.4s ease;"></div>
        </div>

        <div class="matcher-steps-wrapper">
          <!-- Step 1: Legal Issue -->
          <div class="matcher-step active">
            <h3 class="step-title">1. What is the nature of your legal issue?</h3>
            <div class="options-grid">
              <div class="matcher-option category-option" data-value="corporate">
                <svg class="option-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                <span class="option-title">Corporate / Business</span>
                <span class="option-desc">Contracts, Mergers, Partner Disputes</span>
              </div>
              <div class="matcher-option category-option" data-value="ip">
                <svg class="option-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path></svg>
                <span class="option-title">Intellectual Property</span>
                <span class="option-desc">Patents, Trademarks, Copyrights</span>
              </div>
            </div>
          </div>

          <!-- Step 2: Scale of Issue -->
          <div class="matcher-step">
            <h3 class="step-title">2. What is the estimated financial impact?</h3>
            <div class="options-grid">
              <div class="matcher-checkbox skill-checkbox" data-value="under1m">
                <span class="option-title">Under $1 Million</span>
              </div>
              <div class="matcher-checkbox skill-checkbox" data-value="over1m">
                <span class="option-title">$1M - $10 Million</span>
              </div>
              <div class="matcher-checkbox skill-checkbox" data-value="over10m">
                <span class="option-title">Over $10 Million</span>
              </div>
              <div class="matcher-checkbox skill-checkbox" data-value="injunction">
                <span class="option-title">Seeking Injunction / Non-Monetary</span>
              </div>
            </div>
          </div>

          <!-- Step 3: Timeline -->
          <div class="matcher-step">
            <h3 class="step-title">3. Is there an active lawsuit filed?</h3>
            <div class="options-grid">
              <div class="matcher-option timezone-option" data-value="yes">
                <svg class="option-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>
                <span class="option-title">Yes, we are currently in litigation</span>
              </div>
              <div class="matcher-option timezone-option" data-value="no">
                <svg class="option-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
                <span class="option-title">No, seeking counsel to sue or negotiate</span>
              </div>
            </div>
          </div>

          <!-- Final Result View -->
          <div class="matcher-step result-step text-center">
            <div class="success-icon" style="margin: 0 auto 1.5rem; width:80px;height:80px;background:var(--color-accent);border-radius:50%;display:flex;align-items:center;justify-content:center;">
              <svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="#0f172a" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
            </div>
            <h3 class="step-title gradient-text" style="font-size: 2.2rem; margin-bottom: 0.5rem;">Case Evaluation Complete</h3>
            <div class="result-card card-glass" style="margin-top:2rem; padding:2.5rem; text-align:left; border: 1px solid var(--color-accent); border-radius: var(--border-radius-lg); background: var(--bg-primary);">
              <h4 id="matched-role" style="font-size:1.6rem; margin-bottom:1rem; font-family:'Playfair Display', serif;">Your Case Profile Fits Our Expertise</h4>
              <p id="matched-desc" style="color:var(--text-secondary); line-height:1.7; font-size: 1.05rem;">Based on your inputs, your matter aligns with our core trial and corporate capabilities. Alexander Pierce can personally review your file.</p>
              
              <div style="margin-top:2.5rem; text-align: center;">
                <a href="mailto:consult@piercelaw.com" class="btn btn-primary" style="padding: 1rem 3rem; font-size: 1.1rem;">Schedule Confidential Call</a>
              </div>
            </div>
            <button class="btn btn-secondary mt-1" id="matcher-reset" style="margin-top:2rem;">Restart Evaluation</button>
          </div>
        </div>

        <div class="matcher-controls" style="display: flex; justify-content: space-between; margin-top: 3rem; border-top: 1px solid var(--glass-border); padding-top: 1.5rem;">
          <button class="btn btn-secondary" id="matcher-prev" style="display: none; padding: 0.8rem 2rem;">Back</button>
          <button class="btn btn-primary" id="matcher-next" disabled style="padding: 0.8rem 2rem; margin-left: auto;">Next Step</button>
        </div>
      </div>
    </div>
  </section>
"""

# Testimonials
testimonials = """
  <!-- --- TESTIMONIALS CAROUSEL --- -->
  <section class="testimonials section-padding reveal" id="testimonials">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-badge" style="background: rgba(212,175,55,0.1); color: var(--color-accent); border: 1px solid var(--color-accent);">Client Reviews</span>
        <h2 class="section-title">A Record of Success</h2>
        <p class="section-subtitle">Read how Pierce Law has protected the rights and futures of our clients.</p>
      </div>
      
      <div class="carousel-wrapper" style="position: relative; max-width: 900px; margin: 0 auto; padding: 1rem 3rem;">
        <div class="carousel-container" style="overflow: hidden; border-radius: var(--border-radius-lg);">
          <div class="carousel-track" id="testimonial-track" style="display: flex; transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);">
            
            <!-- Slide 1 -->
            <div class="carousel-slide" style="flex: 0 0 100%; padding: 1rem;">
              <div class="testimonial-card card-glass" style="padding: 3rem; text-align: center; border: 1px solid rgba(212,175,55,0.3); background: var(--bg-secondary); border-radius: var(--border-radius-lg);">
                <div style="color: var(--color-accent); font-size: 3rem; line-height: 0; margin-bottom: 2rem;">&#10077;</div>
                <p style="font-size: 1.25rem; font-style: italic; color: var(--text-primary); margin-bottom: 2rem; font-family: 'Playfair Display', serif;">"Alexander Pierce is a force in the courtroom. When our tech firm faced a devastating IP lawsuit, he not only defended us successfully but counter-sued and won."</p>
                <div style="font-weight: 700; font-size: 1rem; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1px;">CEO, Silicon Valley Tech Firm</div>
              </div>
            </div>

            <!-- Slide 2 -->
            <div class="carousel-slide" style="flex: 0 0 100%; padding: 1rem;">
              <div class="testimonial-card card-glass" style="padding: 3rem; text-align: center; border: 1px solid rgba(212,175,55,0.3); background: var(--bg-secondary); border-radius: var(--border-radius-lg);">
                <div style="color: var(--color-accent); font-size: 3rem; line-height: 0; margin-bottom: 2rem;">&#10077;</div>
                <p style="font-size: 1.25rem; font-style: italic; color: var(--text-primary); margin-bottom: 2rem; font-family: 'Playfair Display', serif;">"The level of strategic foresight Pierce Law brings to corporate mergers is unmatched. They saved us millions in regulatory pitfalls."</p>
                <div style="font-weight: 700; font-size: 1rem; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1px;">Managing Director, Capital Group</div>
              </div>
            </div>

            <!-- Slide 3 -->
            <div class="carousel-slide" style="flex: 0 0 100%; padding: 1rem;">
              <div class="testimonial-card card-glass" style="padding: 3rem; text-align: center; border: 1px solid rgba(212,175,55,0.3); background: var(--bg-secondary); border-radius: var(--border-radius-lg);">
                <div style="color: var(--color-accent); font-size: 3rem; line-height: 0; margin-bottom: 2rem;">&#10077;</div>
                <p style="font-size: 1.25rem; font-style: italic; color: var(--text-primary); margin-bottom: 2rem; font-family: 'Playfair Display', serif;">"I was terrified when my business partner attempted a hostile takeover. Alexander stepped in, secured an injunction, and negotiated a buyout in my favor."</p>
                <div style="font-weight: 700; font-size: 1rem; color: var(--color-accent); text-transform: uppercase; letter-spacing: 1px;">Founder, E-Commerce Brand</div>
              </div>
            </div>

          </div>
        </div>

        <!-- Controls -->
        <button id="carousel-prev" style="position: absolute; top: 50%; left: 0; transform: translateY(-50%); background: var(--bg-primary); border: 1px solid var(--color-accent); color: var(--color-accent); width: 44px; height: 44px; border-radius: 50%; cursor: pointer; font-size: 1.2rem; display: flex; align-items: center; justify-content: center; z-index: 10; box-shadow: 0 4px 10px rgba(0,0,0,0.3); transition: all 0.3s ease;">&#10094;</button>
        <button id="carousel-next" style="position: absolute; top: 50%; right: 0; transform: translateY(-50%); background: var(--bg-primary); border: 1px solid var(--color-accent); color: var(--color-accent); width: 44px; height: 44px; border-radius: 50%; cursor: pointer; font-size: 1.2rem; display: flex; align-items: center; justify-content: center; z-index: 10; box-shadow: 0 4px 10px rgba(0,0,0,0.3); transition: all 0.3s ease;">&#10095;</button>
        
        <!-- Dots -->
        <div id="carousel-dots" style="display: flex; justify-content: center; gap: 8px; margin-top: 1.5rem;">
          <div class="dot active" style="width: 10px; height: 10px; border-radius: 50%; background: var(--color-accent); cursor: pointer; transition: all 0.3s ease;"></div>
          <div class="dot" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(212,175,55,0.3); cursor: pointer; transition: all 0.3s ease;"></div>
          <div class="dot" style="width: 10px; height: 10px; border-radius: 50%; background: rgba(212,175,55,0.3); cursor: pointer; transition: all 0.3s ease;"></div>
        </div>
      </div>
    </div>
  </section>
"""

# Floating CTA
floating_cta = """
  <!-- --- FLOATING CTA BANNER --- -->
  <section class="floating-cta reveal" style="margin-bottom: -50px; position: relative; z-index: 10;">
    <div class="container">
      <div class="cta-banner card-glass" style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 2rem; padding: 3rem; background: var(--gradient-brand); border: 1px solid rgba(212,175,55,0.4); border-radius: var(--border-radius-lg);">
        <div class="cta-content" style="flex: 1 1 300px;">
          <h2 class="cta-title" style="font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-bottom: 0.5rem; color: #ffffff;">Your Case Demands the Best.</h2>
          <p class="cta-subtitle" style="font-size: 1.1rem; color: rgba(255,255,255,0.9); margin-bottom: 0;">Contact Pierce Law today for a confidential review of your legal matter.</p>
        </div>
        <div class="cta-action" style="flex: 0 0 auto;">
          <a href="consultation.html" class="btn btn-primary" style="background: var(--color-accent); color: #0f172a; padding: 1.2rem 2.5rem; font-size: 1.1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; border: none; box-shadow: 0 10px 20px rgba(0,0,0,0.3);">Book Consultation</a>
        </div>
      </div>
    </div>
  </section>
"""

# Contact Section
contact_section = """
  <!-- --- CONTACT SECTION --- -->
  <section class="contact section-padding reveal" id="contact" style="background: var(--bg-tertiary);">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-badge" style="background: rgba(212,175,55,0.1); color: var(--color-accent); border: 1px solid var(--color-accent);">Get in Touch</span>
        <h2 class="section-title">Contact Pierce Law</h2>
        <p class="section-subtitle">Reach out via email, phone, or WhatsApp for immediate assistance.</p>
      </div>
      <div class="contact-grid grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 4rem; align-items: center;">
        
        <div class="contact-info">
          <h3 style="font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 1.5rem;">We Are Ready to Defend You</h3>
          <p style="color: var(--text-secondary); margin-bottom: 2rem;">Our legal team is available for emergency injunctions and critical corporate matters.</p>
          
          <div style="display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 2.5rem;">
            <a href="mailto:consult@piercelaw.com" style="display: flex; align-items: center; gap: 1rem; font-size: 1.1rem; font-weight: 500;">
              <svg style="width:24px;height:24px;color:var(--color-accent);" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
              consult@piercelaw.com
            </a>
            <a href="https://wa.me/18005550199" style="display: flex; align-items: center; gap: 1rem; font-size: 1.1rem; font-weight: 500; color: #25D366;">
              <svg style="width:24px;height:24px; fill:currentColor;" viewBox="0 0 448 512"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zM223.9 414.7c-32 0-64-8.6-92-24.9l-6.6-3.9-68.5 18 18.3-66.8-4.3-6.8c-17.8-28.3-27.1-60.8-27.1-94.6 0-103.4 84.1-187.5 187.6-187.5 50.1 0 97.2 19.5 132.7 55 35.4 35.4 54.9 82.5 54.9 132.7 0 103.4-84.1 187.5-187.6 187.5zM326.6 283.5c-5.6-2.8-33.2-16.4-38.3-18.3-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18.3-17.6 22-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-2.1-3.6 2.1-3.5 7.6-14.5 1.4-2.8.7-5.1-.2-7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/></svg>
              WhatsApp Us
            </a>
          </div>

          <div class="social-links" style="display: flex; gap: 1rem;">
            <!-- LinkedIn -->
            <a href="#" style="width: 40px; height: 40px; border-radius: 50%; background: var(--bg-secondary); display: flex; align-items: center; justify-content: center; border: 1px solid var(--glass-border); color: var(--text-primary); transition: all var(--transition-fast);" onmouseover="this.style.background='var(--color-primary)'; this.style.color='white';" onmouseout="this.style.background='var(--bg-secondary)'; this.style.color='var(--text-primary)';">
              <svg style="width:18px;height:18px; fill:currentColor;" viewBox="0 0 448 512"><path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"/></svg>
            </a>
            <!-- Twitter/X -->
            <a href="#" style="width: 40px; height: 40px; border-radius: 50%; background: var(--bg-secondary); display: flex; align-items: center; justify-content: center; border: 1px solid var(--glass-border); color: var(--text-primary); transition: all var(--transition-fast);" onmouseover="this.style.background='var(--color-primary)'; this.style.color='white';" onmouseout="this.style.background='var(--bg-secondary)'; this.style.color='var(--text-primary)';">
              <svg style="width:18px;height:18px; fill:currentColor;" viewBox="0 0 512 512"><path d="M389.2 48h70.6L305.6 224.2 487 464H345L233.6 318.1 106.5 464H35.8L200.7 275.5 26.8 48H172.4L272.9 180.9 389.2 48zM364.4 421.8h39.1L151.1 88h-42L364.4 421.8z"/></svg>
            </a>
            <!-- Facebook -->
            <a href="#" style="width: 40px; height: 40px; border-radius: 50%; background: var(--bg-secondary); display: flex; align-items: center; justify-content: center; border: 1px solid var(--glass-border); color: var(--text-primary); transition: all var(--transition-fast);" onmouseover="this.style.background='var(--color-primary)'; this.style.color='white';" onmouseout="this.style.background='var(--bg-secondary)'; this.style.color='var(--text-primary)';">
              <svg style="width:18px;height:18px; fill:currentColor;" viewBox="0 0 320 512"><path d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"/></svg>
            </a>
          </div>
        </div>

        <div class="contact-form" style="padding: 3rem; background: var(--bg-secondary); border: 2px solid var(--color-accent); border-radius: var(--border-radius-md); box-shadow: var(--hover-shadow); position: relative; overflow: hidden;">
          <h3 id="form-title" style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin-bottom: 0.5rem; text-align: center; transition: opacity 0.3s ease;">Request a Callback</h3>
          <p id="form-desc" style="text-align: center; color: var(--text-secondary); margin-bottom: 2rem; transition: opacity 0.3s ease;">Leave your details below and a senior partner will contact you directly within 24 hours.</p>
          
          <form id="callback-form" style="transition: opacity 0.3s ease, transform 0.3s ease;">
            <div style="margin-bottom: 1.5rem;">
              <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: var(--text-primary);">Your Full Name</label>
              <input type="text" required style="width: 100%; padding: 1rem; border: 2px solid var(--glass-border); border-radius: var(--border-radius-sm); background: var(--bg-primary); color: var(--text-primary); font-size: 1rem;">
            </div>
            <div style="margin-bottom: 1.5rem;">
              <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: var(--text-primary);">Your Email Address</label>
              <input type="email" required style="width: 100%; padding: 1rem; border: 2px solid var(--glass-border); border-radius: var(--border-radius-sm); background: var(--bg-primary); color: var(--text-primary); font-size: 1rem;">
            </div>
            <div style="margin-bottom: 1.5rem;">
              <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: var(--text-primary);">Your Phone Number</label>
              <input type="tel" required style="width: 100%; padding: 1rem; border: 2px solid var(--glass-border); border-radius: var(--border-radius-sm); background: var(--bg-primary); color: var(--text-primary); font-size: 1rem;">
            </div>
            <div style="margin-bottom: 1.5rem;">
              <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: var(--text-primary);">Briefly describe your legal matter...</label>
              <textarea rows="4" required style="width: 100%; padding: 1rem; border: 2px solid var(--glass-border); border-radius: var(--border-radius-sm); background: var(--bg-primary); color: var(--text-primary); font-size: 1rem;"></textarea>
            </div>
            <button type="submit" id="submit-btn" class="btn btn-primary" style="width: 100%; padding: 1.2rem; font-size: 1.1rem; font-weight: bold; position: relative; transition: all 0.3s ease;">
              <span id="btn-text" style="transition: opacity 0.3s ease;">Submit Request</span>
              <div id="btn-spinner" style="display: none; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
                <div style="width: 24px; height: 24px; border: 3px solid rgba(255,255,255,0.3); border-top-color: white; border-radius: 50%; animation: spin 1s linear infinite;"></div>
              </div>
            </button>
          </form>
          
          <div id="callback-success" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: var(--bg-secondary); display: flex; flex-direction: column; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index: 10;">
            <div style="width: 80px; height: 80px; background: rgba(37, 211, 102, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
              <svg id="animated-check" style="width: 40px; height: 40px; color: #25D366; stroke-dasharray: 48; stroke-dashoffset: 48;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
            </div>
            <h4 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; margin-bottom: 1rem; color: var(--text-primary);">Inquiry Confirmed</h4>
            <p style="color: var(--text-secondary); font-size: 1.1rem; max-width: 80%; text-align: center; line-height: 1.6;">Your details have been securely transmitted. Our legal team will review your matter, and a senior partner will contact you directly within 24 hours to discuss your next steps.</p>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

# Core Values
core_values = """
  <!-- --- CORE VALUES --- -->
  <section class="core-values section-padding reveal" style="background: var(--bg-primary);">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-badge" style="background: rgba(212,175,55,0.1); color: var(--color-accent); border: 1px solid var(--color-accent);">Firm Philosophy</span>
        <h2 class="section-title">Our Core Values</h2>
        <p class="section-subtitle">The principles that drive our elite legal representation.</p>
      </div>
      <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
        <div class="card-glass text-center" style="padding: 2.5rem; border: 1px solid rgba(212,175,55,0.3); border-radius: var(--border-radius-lg);">
          <div style="width: 60px; height: 60px; background: rgba(212,175,55,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; color: var(--color-accent);">
            <svg style="width:30px; height:30px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11a4 4 0 118 0c0 1.017-.07 2.019-.203 3m-2.118 6.844A21.88 21.88 0 0015.171 17m3.839 1.132c.645-2.266.99-4.659.99-7.132A8 8 0 008 4.07M3 15.364c.64-1.319 1-2.8 1-4.364 0-1.457.39-2.823 1.07-4"></path></svg>
          </div>
          <h3 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; margin-bottom: 1rem;">Unyielding Integrity</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">We maintain the highest ethical standards in every negotiation and trial, earning the trust of judges, peers, and clients alike.</p>
        </div>
        <div class="card-glass text-center" style="padding: 2.5rem; border: 1px solid rgba(212,175,55,0.3); border-radius: var(--border-radius-lg);">
          <div style="width: 60px; height: 60px; background: rgba(212,175,55,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; color: var(--color-accent);">
            <svg style="width:30px; height:30px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
          </div>
          <h3 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; margin-bottom: 1rem;">Relentless Advocacy</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">We fight aggressively for our clients' interests. We don't just aim to settle; we prepare every case to win at trial.</p>
        </div>
        <div class="card-glass text-center" style="padding: 2.5rem; border: 1px solid rgba(212,175,55,0.3); border-radius: var(--border-radius-lg);">
          <div style="width: 60px; height: 60px; background: rgba(212,175,55,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; color: var(--color-accent);">
            <svg style="width:30px; height:30px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"></path></svg>
          </div>
          <h3 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; margin-bottom: 1rem;">Strategic Excellence</h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem;">Every move we make is calculated. We employ cutting-edge legal strategies to outmaneuver the opposition.</p>
        </div>
      </div>
    </div>
  </section>
"""

# Team Section
team_section = """
  <!-- --- OUR TEAM --- -->
  <section class="team section-padding bg-tertiary">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-badge" style="background: rgba(212,175,55,0.1); color: var(--color-accent); border: 1px solid var(--color-accent);">Legal Roster</span>
        <h2 class="section-title">Meet Our Team</h2>
        <p class="section-subtitle">The brilliant legal minds powering our success.</p>
      </div>
      
      <style>
        .constellation-wrapper {
          position: relative;
          width: 100%;
          max-width: 800px;
          aspect-ratio: 1.2;
          margin: 3rem auto 0;
          background: radial-gradient(circle at center, rgba(30, 60, 114, 0.15) 0%, transparent 60%);
          border-radius: 50%;
        }
        
        .orbit-ring {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          border: 1px dashed rgba(212, 175, 55, 0.25);
          border-radius: 50%;
          z-index: 0;
          animation: spinOrbit 120s linear infinite;
        }
        .orbit-ring-1 { width: 45%; aspect-ratio: 1; }
        .orbit-ring-2 { width: 75%; aspect-ratio: 1; }
        
        .orbit-node {
          position: absolute;
          z-index: 2;
          text-align: center;
          transform: translate(-50%, -50%);
          transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .orbit-node:hover {
          transform: translate(-50%, -50%) scale(1.1);
          z-index: 10;
        }
        
        .orbit-node img {
          border-radius: 50%;
          border: 4px solid var(--color-accent);
          box-shadow: 0 15px 35px rgba(0,0,0,0.5), 0 0 30px rgba(212, 175, 55, 0.15);
          object-fit: cover;
          background: var(--bg-secondary);
          transition: all 0.3s ease;
        }
        
        .orbit-node:hover img {
          border-color: #ffffff;
          box-shadow: 0 20px 40px rgba(0,0,0,0.6), 0 0 40px rgba(212, 175, 55, 0.4);
        }
        
        .orbit-name {
          font-family: var(--font-title);
          font-size: clamp(0.7rem, 2.5vw, 1.3rem);
          margin-top: clamp(0.3rem, 1.5vw, 1rem);
          font-weight: 700;
          color: var(--text-primary);
          text-shadow: 0 2px 4px rgba(0,0,0,0.8);
          white-space: nowrap;
        }
        
        .orbit-role {
          color: var(--color-accent);
          font-size: clamp(0.5rem, 1.5vw, 0.85rem);
          text-transform: uppercase;
          letter-spacing: 1px;
          font-weight: 600;
          white-space: nowrap;
        }

        /* Node Positions & Fluid Sizes */
        .node-center { top: 50%; left: 50%; }
        .node-center img { width: clamp(80px, 22vw, 190px); height: clamp(80px, 22vw, 190px); border-width: clamp(2px, 0.6vw, 5px); }
        
        .node-1 { top: 15%; left: 25%; }
        .node-1 img { width: clamp(60px, 16vw, 140px); height: clamp(60px, 16vw, 140px); border-width: clamp(2px, 0.5vw, 4px); }
        
        .node-2 { top: 25%; left: 85%; }
        .node-2 img { width: clamp(65px, 18vw, 150px); height: clamp(65px, 18vw, 150px); border-width: clamp(2px, 0.5vw, 4px); }
        
        .node-3 { top: 85%; left: 40%; }
        .node-3 img { width: clamp(60px, 16vw, 140px); height: clamp(60px, 16vw, 140px); border-width: clamp(2px, 0.5vw, 4px); }
      </style>
      
      <div class="constellation-wrapper">
        <!-- Background Orbits -->
        <div class="orbit-ring orbit-ring-1"></div>
        <div class="orbit-ring orbit-ring-2"></div>
        
        <!-- Center Node: Alexander Pierce -->
        <div class="orbit-node node-center">
          <img src="images/lawyer_hero_1779391732649.png" alt="Alexander Pierce">
          <h3 class="orbit-name">Alexander Pierce, Esq.</h3>
          <p class="orbit-role">Founder & Managing Partner</p>
        </div>
        
        <!-- Node 1: Sarah Jenkins -->
        <div class="orbit-node node-1">
          <img src="images/lawyer_team_1_1779394155501.png" alt="Sarah Jenkins">
          <h3 class="orbit-name">Sarah Jenkins</h3>
          <p class="orbit-role">Senior Partner</p>
        </div>
        
        <!-- Node 2: David Chen -->
        <div class="orbit-node node-2">
          <img src="images/lawyer_team_2_1779394169178.png" alt="David Chen">
          <h3 class="orbit-name">David Chen</h3>
          <p class="orbit-role">Managing Associate</p>
        </div>
        
        <!-- Node 3: Elena Rodriguez -->
        <div class="orbit-node node-3">
          <img src="images/lawyer_team_3_1779394181506.png" alt="Elena Rodriguez">
          <h3 class="orbit-name">Elena Rodriguez</h3>
          <p class="orbit-role">Senior Paralegal</p>
        </div>
        
      </div>
    </div>
  </section>
"""

# Blog Section
blog_section = """
  <!-- --- LEGAL BLOG --- -->
  <section class="blog section-padding" style="padding-top: 150px; min-height: 80vh;">
    <div class="container">
      <div class="section-header text-center">
        <span class="section-badge" style="background: rgba(212,175,55,0.1); color: var(--color-accent); border: 1px solid var(--color-accent);">Legal Insights</span>
        <h1 class="section-title" style="font-size: 3rem;">Legal Insights & News</h1>
        <p class="section-subtitle">Deep dives into corporate law, intellectual property, and high-stakes litigation.</p>
      </div>
      
      <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 3rem;">
        
        <!-- Blog 1 -->
        <article class="card-glass blog-article" style="border: 1px solid var(--glass-border); border-radius: var(--border-radius-lg); overflow: hidden; transition: all 0.3s ease;">
          <div style="height: 250px; overflow: hidden;">
            <img src="images/blog_legal_1779390997074.png" alt="Corporate Liability" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="padding: 2.5rem; display: flex; flex-direction: column; height: 100%;">
            <span style="font-size: 0.85rem; color: var(--color-accent); text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">Corporate Law &bull; May 12, 2026</span>
            <h3 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; margin: 1rem 0;">Navigating the New Horizons of Corporate Liability</h3>
            <p class="blog-excerpt" style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6; margin-bottom: 2rem; flex-grow: 1;">How recent Supreme Court rulings will impact executive protections and board responsibilities moving forward into the fiscal year.</p>
            <a href="blog-corporate-liability.html" class="btn btn-secondary" style="width: 100%; border-color: rgba(212,175,55,0.3); color: var(--color-accent); text-align: center;">Read Full Article</a>
          </div>
        </article>

        <!-- Blog 2 -->
        <article class="card-glass blog-article" style="border: 1px solid var(--glass-border); border-radius: var(--border-radius-lg); overflow: hidden; transition: all 0.3s ease;">
          <div style="height: 250px; overflow: hidden;">
            <img src="images/blog_contract_1779394196589.png" alt="Contract Negotiations" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="padding: 2.5rem; display: flex; flex-direction: column; height: 100%;">
            <span style="font-size: 0.85rem; color: var(--color-accent); text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">Mergers &bull; Apr 28, 2026</span>
            <h3 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; margin: 1rem 0;">The Art of the High-Stakes Merger Negotiation</h3>
            <p class="blog-excerpt" style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6; margin-bottom: 2rem; flex-grow: 1;">Strategic pitfalls to avoid when structuring buyouts, focusing on avoiding antitrust scrutiny and maximizing shareholder value.</p>
            <a href="blog-mergers.html" class="btn btn-secondary" style="width: 100%; border-color: rgba(212,175,55,0.3); color: var(--color-accent); text-align: center;">Read Full Article</a>
          </div>
        </article>

        <!-- Blog 3 -->
        <article class="card-glass blog-article" style="border: 1px solid var(--glass-border); border-radius: var(--border-radius-lg); overflow: hidden; transition: all 0.3s ease;">
          <div style="height: 250px; overflow: hidden;">
            <img src="images/blog_ai_1779391039373.png" alt="AI IP Law" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="padding: 2.5rem; display: flex; flex-direction: column; height: 100%;">
            <span style="font-size: 0.85rem; color: var(--color-accent); text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">Intellectual Property &bull; Apr 15, 2026</span>
            <h3 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; margin: 1rem 0;">Protecting Trade Secrets in the Age of AI</h3>
            <p class="blog-excerpt" style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6; margin-bottom: 2rem; flex-grow: 1;">As AI models scrape data, how can Fortune 500s safeguard their proprietary algorithms and confidential IP?</p>
            <a href="blog-ai-ip.html" class="btn btn-secondary" style="width: 100%; border-color: rgba(212,175,55,0.3); color: var(--color-accent); text-align: center;">Read Full Article</a>
          </div>
        </article>

        <!-- Blog 4 -->
        <article class="card-glass blog-article" style="border: 1px solid var(--glass-border); border-radius: var(--border-radius-lg); overflow: hidden; transition: all 0.3s ease;">
          <div style="height: 250px; overflow: hidden;">
            <img src="images/blog_ediscovery_1779391012179.png" alt="E-Discovery" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="padding: 2.5rem; display: flex; flex-direction: column; height: 100%;">
            <span style="font-size: 0.85rem; color: var(--color-accent); text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">Litigation &bull; Mar 30, 2026</span>
            <h3 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; margin: 1rem 0;">E-Discovery: Winning the Pre-Trial Data War</h3>
            <p class="blog-excerpt" style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6; margin-bottom: 2rem; flex-grow: 1;">Why modern commercial litigation is won or lost during the electronic discovery phase, and how to weaponize data retrieval.</p>
            <a href="blog-ediscovery.html" class="btn btn-secondary" style="width: 100%; border-color: rgba(212,175,55,0.3); color: var(--color-accent); text-align: center;">Read Full Article</a>
          </div>
        </article>

        <!-- Blog 5 -->
        <article class="card-glass blog-article" style="border: 1px solid var(--glass-border); border-radius: var(--border-radius-lg); overflow: hidden; transition: all 0.3s ease;">
          <div style="height: 250px; overflow: hidden;">
            <img src="images/hero_office_1779390764930.png" alt="Injunctions" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="padding: 2.5rem; display: flex; flex-direction: column; height: 100%;">
            <span style="font-size: 0.85rem; color: var(--color-accent); text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">Strategy &bull; Mar 12, 2026</span>
            <h3 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; margin: 1rem 0;">The Tactical Use of Preliminary Injunctions</h3>
            <p class="blog-excerpt" style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6; margin-bottom: 2rem; flex-grow: 1;">Freezing assets and stopping bleeding early. A case study on why aggressive early maneuvers dictate settlement outcomes.</p>
            <a href="blog-injunctions.html" class="btn btn-secondary" style="width: 100%; border-color: rgba(212,175,55,0.3); color: var(--color-accent); text-align: center;">Read Full Article</a>
          </div>
        </article>

      </div>
    </div>
  </section>
"""

# Footer
footer = f"""
  <!-- --- FOOTER --- -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid grid">
        <div class="footer-brand">
          <a href="index.html" class="logo mb-1">
            <img src="images/lawyer_logo_1779391715094.png" alt="Pierce Law Logo" style="height:40px; border-radius:8px;">
            <div class="logo-text">Pierce<span>Law</span></div>
          </a>
          <p class="footer-desc" style="margin-top: 1rem;">{tagline} High-stakes litigation and elite corporate representation across the nation.</p>
        </div>
        <div class="footer-links">
          <h4>Firm</h4>
          <ul>
            <li><a href="about-attorney.html">Alexander Pierce</a></li>
            <li><a href="case-results.html">Case Results</a></li>
            <li><a href="testimonials.html">Testimonials</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h4>Practice Areas</h4>
          <ul>
            <li><a href="practice-areas.html#corporate">Corporate Law</a></li>
            <li><a href="practice-areas.html#litigation">Commercial Litigation</a></li>
            <li><a href="practice-areas.html#ip">Intellectual Property</a></li>
          </ul>
        </div>
        <div class="footer-contact">
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:consult@piercelaw.com">consult@piercelaw.com</a></li>
            <li><a href="tel:+18005550199">1-800-555-0199</a></li>
            <li style="color: var(--text-secondary); margin-top: 0.5rem;">One World Trade Center<br>Suite 4500, NY 10007</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 {brand_name}. All rights reserved. <br><span style="font-size:0.8rem; color:var(--text-tertiary);">Attorney Advertising. Prior results do not guarantee a similar outcome.</span></p>
      </div>
    </div>
  </footer>

  <script src="app.js"></script>
</body>
</html>
"""

# Single Blog Post Template
def generate_blog_post(title, category, date, image_path, content_html):
    return f"""
  <section class="single-blog section-padding" style="padding-top: 120px;">
    <div class="container" style="max-width: 900px; margin: 0 auto;">
      <a href="legal-blog.html" style="display: inline-flex; align-items: center; gap: 0.5rem; color: var(--color-accent); font-weight: 600; text-decoration: none; margin-bottom: 2rem;">&larr; Back to Insights</a>
      
      <div style="margin-bottom: 2.5rem;">
        <span style="font-size: 0.9rem; color: var(--color-accent); text-transform: uppercase; font-weight: 600; letter-spacing: 1px;">{category} &bull; {date}</span>
        <h1 style="font-family: 'Playfair Display', serif; font-size: clamp(2rem, 5vw, 3.5rem); line-height: 1.1; margin: 1rem 0;">{title}</h1>
      </div>
      
      <div style="width: 100%; height: clamp(250px, 40vw, 450px); border-radius: var(--border-radius-lg); overflow: hidden; margin-bottom: 3rem; box-shadow: var(--card-shadow); border: 1px solid var(--glass-border);">
        <img src="{image_path}" alt="{title}" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
      
      <div class="blog-body" style="font-size: 1.15rem; line-height: 1.8; color: var(--text-secondary);">
        {content_html}
      </div>
      
      <div style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--glass-border); text-align: center;">
        <h3 style="font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 1rem;">Need Counsel on this Issue?</h3>
        <a href="consultation.html" class="btn btn-primary" style="padding: 1rem 2rem;">Schedule a Free Consultation</a>
      </div>
    </div>
  </section>
"""

# Define Blog Posts
blog_1_content = """
<p style="margin-bottom: 1.5rem;">The landscape of corporate liability has shifted dramatically following the latest precedent-setting rulings. For decades, the corporate veil provided a nearly impenetrable shield for board members and C-suite executives, protecting personal assets from corporate misdeeds.</p>
<p style="margin-bottom: 1.5rem;">However, a new wave of legal interpretation suggests that willful ignorance or negligence in regulatory compliance can pierce this veil. Executives are now being held to a higher standard of active oversight. Failure to implement robust compliance mechanisms is no longer just a corporate fine—it's a personal liability risk.</p>
<h3 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin: 2.5rem 0 1rem; color: var(--text-primary);">The New Standard of Oversight</h3>
<p style="margin-bottom: 1.5rem;">Recent federal rulings have clarified that "Caremark claims"—lawsuits alleging a board failed to oversee corporate operations—are becoming easier for plaintiffs to survive early dismissal. If a company operates in a highly regulated industry, the board must proactively monitor core compliance risks.</p>
<p style="margin-bottom: 1.5rem;">At Pierce Law, we are proactively auditing our clients' governance structures. We strongly advise all boards to immediately review their D&O insurance policies and schedule a compliance stress-test before the end of Q3.</p>
"""

blog_2_content = """
<p style="margin-bottom: 1.5rem;">A successful merger is rarely just about capital; it's about control, legacy, and navigating regulatory minefields. When structuring a buyout, the initial term sheet is merely the opening salvo in a grueling war of attrition.</p>
<p style="margin-bottom: 1.5rem;">One of the most critical pitfalls we observe is the failure to adequately anticipate antitrust pushback. If your merger creates a dominant market force, regulators will scrutinize every email and internal memo. Defensive legal strategy must begin the moment the M&A idea is conceived, not after the FTC raises an eyebrow.</p>
<h3 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin: 2.5rem 0 1rem; color: var(--text-primary);">Earn-Outs and Ambiguity</h3>
<p style="margin-bottom: 1.5rem;">Furthermore, structuring earn-outs and golden parachutes requires meticulous drafting to prevent post-merger litigation. Ambiguity is the enemy of the deal. At Pierce Law, our drafting is impenetrable, ensuring that when the ink dries, our clients hold all the leverage.</p>
"""

blog_3_content = """
<p style="margin-bottom: 1.5rem;">The rapid proliferation of Generative AI has created a nightmare scenario for intellectual property protection. Large Language Models continuously scrape the digital landscape, often ingesting proprietary code, unreleased patents, and sensitive trade secrets inadvertently exposed by employees.</p>
<p style="margin-bottom: 1.5rem;">Traditional NDAs are no longer sufficient. Companies must deploy aggressive internal ring-fencing protocols. If an employee inputs a proprietary algorithm into a public AI tool to "optimize" it, that algorithm may instantly enter the public domain, obliterating its trade secret status under the Uniform Trade Secrets Act (UTSA).</p>
<h3 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin: 2.5rem 0 1rem; color: var(--text-primary);">Establishing Clean Rooms</h3>
<p style="margin-bottom: 1.5rem;">We are currently representing several tech conglomerates in establishing "clean room" development environments and drafting aggressive cease-and-desist mandates against AI firms found training on our clients' copyrighted frameworks.</p>
"""

blog_4_content = """
<p style="margin-bottom: 1.5rem;">Trials are rarely won through dramatic courtroom cross-examinations. They are won months earlier, buried beneath terabytes of Slack messages, fragmented emails, and metadata. Welcome to the modern E-Discovery war.</p>
<p style="margin-bottom: 1.5rem;">Opposing counsel often uses discovery requests as a weapon of financial attrition, demanding impossibly broad data pulls to force a settlement. Conversely, hiding or deleting data (spoliation) carries catastrophic sanctions, including automatic default judgments.</p>
<h3 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin: 2.5rem 0 1rem; color: var(--text-primary);">Forensic Defense</h3>
<p style="margin-bottom: 1.5rem;">Pierce Law utilizes proprietary AI-driven forensic tools to slash discovery costs while uncovering the "smoking gun" communications that opposing counsel attempts to bury. If you are facing litigation, your data preservation protocols must be activated immediately. Silence is not golden; it's discoverable.</p>
"""

blog_5_content = """
<p style="margin-bottom: 1.5rem;">When a rogue former executive attempts to steal your client list, or a competitor launches a copycat product, waiting for a trial date is corporate suicide. The damage will be done.</p>
<p style="margin-bottom: 1.5rem;">A Preliminary Injunction is the legal equivalent of a tactical strike. By convincing a judge that irreparable harm is imminent, we can legally freeze the opposition's operations, assets, or product launches overnight.</p>
<h3 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin: 2.5rem 0 1rem; color: var(--text-primary);">Burden of Proof</h3>
<p style="margin-bottom: 1.5rem;">Securing an injunction requires an overwhelming initial burden of proof. It forces the opposition onto the defensive immediately, often bringing them to the settlement table within days rather than years. Pierce Law has secured over 40 emergency injunctions in federal courts nationwide.</p>
"""

pages = {
    'index.html': f"{header}\n{hero}\n{stats}\n{core_values}\n{practice_areas}\n{matcher}\n{team_section}\n{testimonials}\n{contact_section}\n{floating_cta}\n{footer}",
    'about-attorney.html': f"{header}\n{stats}\n{core_values}\n{team_section}\n{contact_section}\n{floating_cta}\n{footer}",
    'practice-areas.html': f"{header}\n{practice_areas}\n{contact_section}\n{floating_cta}\n{footer}",
    'case-results.html': f"{header}\n{testimonials}\n{contact_section}\n{floating_cta}\n{footer}",
    'consultation.html': f"{header}\n{matcher}\n{contact_section}\n{footer}",
    'legal-blog.html': f"{header}\n{blog_section}\n{contact_section}\n{floating_cta}\n{footer}",
    'blog-corporate-liability.html': f"{header}\n{generate_blog_post('Navigating the New Horizons of Corporate Liability', 'Corporate Law', 'May 12, 2026', 'images/blog_legal_1779390997074.png', blog_1_content)}\n{contact_section}\n{footer}",
    'blog-mergers.html': f"{header}\n{generate_blog_post('The Art of the High-Stakes Merger Negotiation', 'Mergers', 'Apr 28, 2026', 'images/blog_contract_1779394196589.png', blog_2_content)}\n{contact_section}\n{footer}",
    'blog-ai-ip.html': f"{header}\n{generate_blog_post('Protecting Trade Secrets in the Age of AI', 'Intellectual Property', 'Apr 15, 2026', 'images/blog_ai_1779391039373.png', blog_3_content)}\n{contact_section}\n{footer}",
    'blog-ediscovery.html': f"{header}\n{generate_blog_post('E-Discovery: Winning the Pre-Trial Data War', 'Litigation', 'Mar 30, 2026', 'images/blog_ediscovery_1779391012179.png', blog_4_content)}\n{contact_section}\n{footer}",
    'blog-injunctions.html': f"{header}\n{generate_blog_post('The Tactical Use of Preliminary Injunctions', 'Strategy', 'Mar 12, 2026', 'images/hero_office_1779390764930.png', blog_5_content)}\n{contact_section}\n{footer}",
}

for filename, content in pages.items():
    write_file(filename, content)
    print(f"Generated {filename}")
