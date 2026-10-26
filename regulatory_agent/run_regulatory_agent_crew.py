from crewai import Agent, Crew, Process, Task, LLM
import requests
import os


# Define and initialize 'requirements.md' right at the beginning
output_filename = "./requirements/compliance_matrix.md"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write("# Charpentier Shipyard — MASS Concept Study\n\n*Status: Initializing agentic workflow and fetching requirements...*\n")
print(f"Created initial placeholder file: {output_filename}")

# Initialize Gemini via CrewAI's native LLM wrapper with a current model name
gemini_llm = LLM(
    model="gemini/gemini-3.8-flash",
    temperature=0.2
)

# Define raw URLs to your markdown files on GitHub
github_files = {
    "approach": "https://raw.githubusercontent.com/draronnax83-cmd/MASS-Concept-Study-Charpentier/refs/heads/main/Agentic-Engineering-Approach.md",
    "task": "https://raw.githubusercontent.com/draronnax83-cmd/MASS-Concept-Study-Charpentier/refs/heads/main/Readme.md",
    "tobedone": "https://raw.githubusercontent.com/draronnax83-cmd/MASS-Concept-Study-Charpentier/refs/heads/main/Team-Responsibilities.md"
}
      
fetched_content = ""
for name, url in github_files.items():
    try:
        response = requests.get(url)
        response.raise_for_status()
        fetched_content += f"\n\n--- CONTENT FROM {name.upper()} ---\n{response.text}"
        print(f"Successfully loaded: {name}")
    except Exception as e:
        print(f"Warning: Could not fetch {name} from GitHub ({e})")

# Define agent
regulatory_analyst = Agent(
    role="Senior Maritime Regulatory Compliance Specialist",
    goal="Ensure the concept-level Uncrewed Surface Vessel (USV) / Maritime Autonomous Surface System (MASS) strictly complies with relevant international maritime regulations review, EU regulatory mapping, NATO standards assessment, and MASS guidance.",
    backstory="You are an expert in international maritime law, cybersecurity, safety management, and class rules (DNV/LR), specializing in autonomous and remotely supervised surface vessels (MASS/USV).",
    verbose=True,
    llm=gemini_llm
)

# Define Task 
task_regulatory = Task(
    description="Analyze concept-level Uncrewed Surface Vessel (USV) / MASS operations, including autonomous and remotely supervised modes, under the IMO MASS Code, COLREGs, SOLAS, EU regulations, and NATO standards based on the provided repository context.",
    expected_output=(
        "A comprehensive markdown table containing all gathered requirements. "
        "Each requirement must include: Req ID (e.g., REQ-MASS-001), Regulation/Standard, "
        "Requirement Title, Description, and the target Project Stage: "
        "Regulatory Analysis, Requirements Derivation, SysML Modeling (SysON), System Architecture, "
        "Concept Design (FreeCAD), Visualization (Blender), UI/Digital Twin (Lovable), or Integrated MASS Demonstrator."
    ),
    agent=regulatory_analyst
)

# Assemble the Crew 
mass_crew = Crew(
    agents=[regulatory_analyst],
    tasks=[task_regulatory],
    verbose=True
)

if __name__ == "__main__":
    print("## Starting Charpentier Shipyard MASS Workflow ##")
    result = mass_crew.kickoff()
   # print("\n\n## Final Agent Output ##")
   # print(result)
    
  # Overwrite 'requirement.md' with the final agent results when complete
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(str(result))
        
    print(f"\n\n## Success! Final output saved locally to: {output_filename} ##")