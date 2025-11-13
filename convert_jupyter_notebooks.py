import json
import sys
import datetime

if __name__ == '__main__':
    if len(sys.argv) > 1: # we check if we received any argument
        if sys.argv[1] == "supports":
            sys.exit(0)

    # load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)


    with open("content.json", "w") as fh:
       json.dump(book, fh, indent=2)
    with open("context.json", "w") as fh:
        json.dump(context, fh, indent=2)


    # locate the file generated-page.md and modify its content
    # now = datetime.datetime.now()
    # found = False
    # for chapter in book['sections']:
    #     if 'Chapter' in chapter:
    #         for item in chapter['Chapter']['sub_items']:
    #             if 'Chapter' in item:
    #                 if item['Chapter']['path'] == 'generated-page.md':
    #                     item['Chapter']['content'] = 'Generated at <b>{}</b>'.format(now.strftime("%Y-%m-%d %H:%M:%S"))
    #                     found = True

    # #with open("after.json", "w") as fh:
    # #   json.dump(book, fh, indent=2)

    # # Hard fail if we did not find the page and could not do our job
    # if not found:
    #     exit("Page not found")

    print(json.dumps(book))

