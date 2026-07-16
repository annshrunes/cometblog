import os
import re
import shutil

# Paths
posts_dir = "/home/comet/Documents/cometblog/content/posts"
attachments_dir = "/home/comet/Documents/webb/Attachments"
static_images_dir = "/home/comet/Documents/cometblog/static/images"
image_extensions = {"png", "gif", "jpg", "jpeg", "webp", "bmp", "tif", "tiff", "svg", "avif", "heic", "heif", "ico"}

# Step 1: Process each markdown file under the posts tree
for root, _, filenames in os.walk(posts_dir):
    for filename in filenames:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)

            with open(filepath, "r") as file:
                content = file.read()

            # Step 2: Find all image links for common image formats.
            images = re.findall(r'\[\[([^]]+\.[^]]+)\]\]', content, flags=re.IGNORECASE)

            # Step 3: Replace image links and ensure URLs are correctly formatted
            for image in images:
                extension = os.path.splitext(image)[1].lower().lstrip('.')
                if extension not in image_extensions:
                    continue

                # Prepare the Markdown-compatible link with %20 replacing spaces
                markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
                content = content.replace(f"![[{image}]]", markdown_image)
                content = content.replace(f"[[{image}]]", markdown_image)

                # Step 4: Copy the image to the Hugo static/images directory if it exists
                image_source = os.path.join(attachments_dir, image)
                if os.path.exists(image_source):
                    shutil.copy(image_source, static_images_dir)

            # Step 5: Write the updated content back to the markdown file
            with open(filepath, "w") as file:
                file.write(content)

print("Markdown files processed and images copied successfully.")
