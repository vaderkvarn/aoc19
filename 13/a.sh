./wrapper.py input | awk 'NR%3==0 && $0 == 2' | wc -l
