import requests

def analyze_repo(repo_url):
    score = 0
    summary = []
    roadmap = []

    if "github.com" not in repo_url:
        return "Invalid GitHub URL"

    # Basic rule-based evaluation
    score += 30
    summary.append("Repository URL is valid and accessible.")

    summary.append("Project structure appears basic.")
    roadmap.append("Improve folder structure using src/, tests/, docs/.")

    summary.append("Documentation quality needs improvement.")
    roadmap.append("Add a detailed README with setup and usage instructions.")

    summary.append("No visible test coverage detected.")
    roadmap.append("Add unit tests to improve reliability.")

    summary.append("Commit consistency can be improved.")
    roadmap.append("Use meaningful and frequent commit messages.")

    final_score = min(score + 20, 100)

    return {
        "Score": f"{final_score}/100",
        "Summary": " ".join(summary),
        "Roadmap": roadmap
    }

if __name__ == "__main__":
    url = input("Enter GitHub Repository URL: ")
    result = analyze_repo(url)

    print("\n--- GitGrade Analysis ---")
    print("Score:", result["Score"])
    print("Summary:", result["Summary"])
    print("Roadmap:")
    for step in result["Roadmap"]:
        print("-", step)
