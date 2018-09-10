from xiblint.rules import Rule


class Images(Rule):
    """
    Checks for images
    """
    def check(self, context):  # type: (Rule, xiblint.xibcontext.XibContext) -> None
        if ("LaunchScreen-" not in context.path):
            for image in context.tree.findall("./resources/image"):
                title = image.get("name")
                context.error(image, "Image exists with name: {}", title)
