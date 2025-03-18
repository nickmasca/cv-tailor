def generate_diff(original_text, modified_text):
    import difflib

    # Split the texts into lines for comparison
    original_lines = original_text.splitlines(keepends=True)
    modified_lines = modified_text.splitlines(keepends=True)

    # Create a diff object
    diff = difflib.unified_diff(original_lines, modified_lines, lineterm='', fromfile='Original CV', tofile='Tailored CV')

    # Generate the Markdown formatted diff
    markdown_diff = '```diff\n' + ''.join(diff) + '```\n'

    return markdown_diff