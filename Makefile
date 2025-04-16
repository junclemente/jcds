# Set VERSION at the command line like: make release VERSION=0.2.5
VERSION ?= $(error Please provide a version like: make release VERSION=0.2.5)

## 🏷️ Full release automation
release:
	@echo "🔖 Releasing version v$(VERSION)..."
	@git-cliff --config .gitcliff.toml --unreleased --tag v$(VERSION) --prepend CHANGELOG.md
	@git add CHANGELOG.md
	@git commit -m "chore: release v$(VERSION)"
	@git tag v$(VERSION)
	@git push origin main --tags
	@echo "✅ Release v$(VERSION) completed."

## 📝 Safe dry-run preview (no commit, no file changes)
changelog:
	@echo "📝 Previewing changelog for v$(VERSION) (no file will be modified)"
	@git-cliff --config .gitcliff.toml --unreleased --tag v$(VERSION)

changelog-save:
	@echo "💾 Saving changelog for v$(VERSION) to CHANGELOG.md (without tagging)"
	@git-cliff --config .gitcliff.toml --unreleased --tag v$(VERSION) --prepend CHANGELOG.md
