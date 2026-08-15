# ---
# title: justfile for ds-ml-project_flight-delay-prediction
# ---

# ---

default:
    @just --list --unsorted

# Bundle presentation HTML via monolith
presentation:
    monolith --output "docs/presentation.html" "docs/presentation/index.html"
