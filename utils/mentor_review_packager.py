# 📦 Script mentor_review_packager.py — archivage des feedbacks
import shutil
import os

def package_mentor_reviews(source_files=None, output_path="delivery/mentor_reviews.zip"):
    if source_files is None:
        source_files = [
            "config/mentor_feedback.yaml",
            "exports/mentor_validations.md",
            "exports/bot_certificate.md"
        ]

    temp_dir = "delivery/temp_reviews"
    os.makedirs(temp_dir, exist_ok=True)

    for f in source_files:
        shutil.copy(f, os.path.join(temp_dir, os.path.basename(f)))

    shutil.make_archive(output_path.replace(".zip", ""), 'zip', temp_dir)
    shutil.rmtree(temp_dir)

    print(f"✅ mentor_reviews.zip généré dans {output_path}")

if __name__ == "__main__":
    package_mentor_reviews()
