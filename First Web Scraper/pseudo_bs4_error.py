try:
    badcontent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print('Tag was not found!')
else:
    if badcontent == None:
        print('Tag was not found!')
    else:
        print(badcontent)