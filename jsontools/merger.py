import json
from glob import glob

def merge_files(input_file_pattern, output_file, transform_function=None, indent=None):
    """
    Merge json objects stored in a directory specified by :input_file_pattern
    :param input_file_pattern: The file pattern using glob convention
    :param output_file:
    :param transform_function:
    :param indent:
    :return:
    """
    elements = []
    for g in glob(input_file_pattern):
        with open(g, "r") as r:
            document = json.load(r)
            if type(document) == dict:
                if transform_function is not None:
                    add, new_item = transform_function(document)
                    if add:
                        elements.append(new_item)
                else:
                    elements.append(document)
            else:
                for d in document:
                    if transform_function is not None:
                        add, new_item = transform_function(d)
                        if add:
                            elements.append(new_item)
                    else:
                        elements.append(d)
    with open(output_file, "w") as w:
        json.dump(elements, w, indent=indent)
    return len(elements)