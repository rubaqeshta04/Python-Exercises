def build_profile(name, **details):
    profile = {"name": name}
    profile.update(details)
    return profile
    

print(build_profile("Ali", age=20, country="Palestine", job="student"))    