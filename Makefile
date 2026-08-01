.PHONY: help new

help:
	@echo 'Usage: make new TITLE="3. Longest Substring Without Repeating Characters"'

new:
	@if [ -z "$(strip $(TITLE))" ]; then \
		echo 'Error: TITLE is required.' >&2; \
		echo 'Usage: make new TITLE="3. Longest Substring Without Repeating Characters"' >&2; \
		exit 1; \
	fi; \
	dir_name="$$(printf '%s' "$(TITLE)" | python3 -c 'import re, sys, unicodedata; title = unicodedata.normalize("NFKD", sys.stdin.read()).encode("ascii", "ignore").decode().lower(); name = re.sub(r"[^a-z0-9]+", "_", title).strip("_"); print(name if name and not name[0].isdigit() else "problem_" + name)')"; \
	if [ -z "$$dir_name" ]; then \
		echo 'Error: TITLE must contain at least one ASCII letter or digit.' >&2; \
		exit 1; \
	fi; \
	mkdir -p "$$dir_name"; \
	if [ ! -e "$$dir_name/README.md" ]; then \
		printf '# %s\n' "$(TITLE)" > "$$dir_name/README.md"; \
	fi; \
	for file in solve_1.py solve_2.py solve_3.py; do \
		if [ ! -e "$$dir_name/$$file" ]; then \
			touch "$$dir_name/$$file"; \
		fi; \
	done; \
	echo "Created: $$dir_name"
