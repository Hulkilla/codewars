
study = ""
study_list = study.split(sep = " ")


for x in range(len(study_list)):
    study_list[x] = study_list[x].capitalize()

joined_s = "".join(study_list)
print(joined_s)


# case clever
def camel_case(string):
    return string.title().replace(" ", "")
