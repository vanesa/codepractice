def mirror_string(phrase):

	chars = phrase

	if not chars:
		return ''

	return chars[-1] + mirror_string(chars[:-1])

print mirror_string('Hello world!')
