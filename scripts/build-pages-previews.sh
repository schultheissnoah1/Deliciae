#!/usr/bin/env bash
set -euo pipefail

scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT

while IFS=$'\t' read -r number sha; do
  [[ "$number" =~ ^[0-9]+$ && "$sha" =~ ^[0-9a-f]{40}$ ]] || exit 1
  source_dir="$scratch/$number"
  destination="_site/previews/pr-$number"
  mkdir -p "$source_dir"

  # Use the main branch's dependencies and safe mode when rendering PR content.
  if git fetch --no-tags --depth=1 origin "$sha" &&
    git archive "$sha" site | tar -x -C "$source_dir" &&
    JEKYLL_ENV=production bundle exec jekyll build --safe --source "$source_dir/site" \
      --destination "$source_dir/output" --baseurl "/Deliciae/previews/pr-$number" &&
    [[ -f "$source_dir/output/index.html" ]]; then
    mkdir -p "$(dirname "$destination")"
    mv "$source_dir/output" "$destination"
  else
    printf '::warning::Could not build the GitHub Pages preview for PR #%s\n' "$number"
  fi
done < "$1"
