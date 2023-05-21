
def find_text(element, selector_type, selector, attribute = None):
    text = ""
    try:
        if attribute:
            text = element.find_element(selector_type, selector).get_attribute(attribute)
        else:
            text = element.find_element(selector_type, selector).text

    except Exception as e:
        pass
    return text