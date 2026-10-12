function noted() {
    for file in "$HOME/notes/src"/*.md
    do 
        python3 "$HOME/notes/build/main.py" "$file"
    done

    inotifywait -mrqe modify --exclude "/\..+" --format "%w%f" "$HOME/notes/src" | while read file
    do
        [[ "$file" == *.md ]] || continue
        python3 "$HOME/notes/build/main.py" "$file"
    done
}

