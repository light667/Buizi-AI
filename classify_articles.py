import os
import shutil
from pathlib import Path

# Configuration
articles_dir = "articles"
data_dir = "data"
categories = {
    "marketing_strategy": [
        "loop marketing", "strategy", "marketing playbook", "campaign", "growth",
        "marketing planning", "procurement", "agency partnership", "b2b", "funnel",
        "customer acquisition", "marketing mix", "brand strategy", "long-term",
        "marketing framework", "value creation", "strategic alignment"
    ],
    "social_media": [
        "tiktok", "social", "platform", "advertising", "ads manager", "cpms",
        "influencer", "creator", "audience", "engagement", "paid media", "auction",
        "conversion rate", "feed", "budget", "trending", "viral"
    ],
    "templates": [
        "tips", "tools", "guide", "how to", "tutorial", "step", "best practice",
        "trick", "method", "framework", "template", "prompt", "shortcut",
        "productivity", "optimization", "workspace"
    ],
    "ecommerce": [
        "ecommerce", "customer churn", "appstore", "purchase", "conversion",
        "product", "seller", "transaction", "ifood", "checkout", "payment",
        "customer retention", "subscription"
    ],
    "local_business": [
        "local", "small business", "coffee shop", "seo", "google business",
        "website traffic", "local seo", "owner", "region", "community"
    ],
    "copywriting": [
        "copy", "writing", "message", "content", "brand voice", "tone",
        "value proposition", "headline", "email", "persuasion", "storytelling",
        "narrative", "brand story", "communication"
    ],
    "market_data": [
        "survey", "research", "data", "statistic", "percentage", "analysis",
        "report", "finding", "insight", "metric", "benchmark", "study",
        "trend", "forecast", "number"
    ],
    "case_studies": [
        "case study", "example", "success story", "result", "client",
        "implementation", "real world", "scenario", "business case"
    ]
}

def read_file(filepath):
    """Read file content"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read().lower()
    except:
        return ""

def classify_article(content):
    """Classify article based on keywords"""
    if not content:
        return "market_data"  # default category
    
    # Count keyword matches for each category
    category_scores = {}
    for category, keywords in categories.items():
        score = sum(1 for keyword in keywords if keyword in content)
        category_scores[category] = score
    
    # Return category with highest score, default to market_data
    best_category = max(category_scores, key=category_scores.get)
    if category_scores[best_category] == 0:
        return "market_data"
    return best_category

def main():
    # Get all files from articles folder
    articles_path = Path(articles_dir)
    article_files = sorted([f for f in articles_path.glob("*.txt")])
    
    if not article_files:
        print("No article files found!")
        return
    
    # Classification results
    classification_results = {}
    
    print(f"Found {len(article_files)} article files to classify...\n")
    
    for article_file in article_files:
        # Read content
        content = read_file(article_file)
        
        # Classify
        category = classify_article(content)
        
        # Store result
        if category not in classification_results:
            classification_results[category] = []
        classification_results[category].append(article_file.name)
        
        print(f"✓ {article_file.name} → {category}")
        
        # Copy file to category folder
        dest_folder = Path(data_dir) / category
        dest_folder.mkdir(parents=True, exist_ok=True)
        dest_path = dest_folder / article_file.name
        
        # Copy file
        shutil.copy2(article_file, dest_path)
    
    # Print summary
    print("\n" + "="*60)
    print("CLASSIFICATION SUMMARY")
    print("="*60)
    
    for category in sorted(classification_results.keys()):
        files = classification_results[category]
        print(f"\n{category.upper()} ({len(files)} files):")
        for filename in sorted(files):
            print(f"  - {filename}")
    
    print(f"\nTotal files classified: {len(article_files)}")

if __name__ == "__main__":
    main()
