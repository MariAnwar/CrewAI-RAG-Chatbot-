import regex as re

def get_referenced_images(self, referenced_pages, view_mode="Extracted Images"):
        """
        Returns a dictionary of image paths for the referenced pages.
        Does NOT display anything (pure backend logic).
        """
        result = {"mode": view_mode, "pages": {}}

        if not referenced_pages:
            return result  # empty dict

        if view_mode == "Extracted Images":
            if not self.pdf_images_dir.exists():
                return result

            for page in sorted(referenced_pages):
                pattern = re.compile(rf"^page{page}_img\d+\.(jpg|jpeg|png)$", re.IGNORECASE)
                matching_images = [
                    str(f) for f in self.pdf_images_dir.iterdir() if pattern.match(f.name)
                ]
                result["pages"][page] = matching_images

        elif view_mode == "Full PDF Pages":
            if not self.pdf_pages_dir.exists():
                return result

            for page in sorted(referenced_pages):
                page_path = self.pdf_pages_dir / f"page{page}.jpg"
                if page_path.exists():
                    result["pages"][page] = [str(page_path)]
                else:
                    result["pages"][page] = []

        return result