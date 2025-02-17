mkdir -p book_covers_cropped_256

for file in book-covers/*.jpg; do
    if [ -f "$file" ]; then  # Check if file exists
        filename=$(basename "$file")
        ffmpeg -i "$file" -vf "crop=min(iw\,ih):min(iw\,ih),scale=256:256" "book_covers_cropped_256/$filename"
    fi
done