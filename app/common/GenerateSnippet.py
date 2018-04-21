def SplitContentIntoLines(content, endOfLineSequence):
	return content.split(endOfLineSequence)

def EscapeDoubleQuotes(content):
	escapeStr = '\\"'
	return content.replace('"', escapeStr)

def ReplaceSpacesWithTabDelimiter(content, tabSize):
	tabIdentifier = tabSize * ' '
	tabDelimiter = '\\t'
	return content.replace(tabIdentifier, tabDelimiter)

def AddDoubleQuotes(content):
	return '"' + str(content) + '"'

def GenerateSnippetLines(lines, tabSize):
	snippetLines = []
	for line in lines:
		line = ReplaceSpacesWithTabDelimiter(line, tabSize)
		line = EscapeDoubleQuotes(line)
		line = AddDoubleQuotes(line)
		snippetLines.append(line)
	return snippetLines

def BuildSnippetBody(snippetLines):
	bodyLineseparator = ',\n\t\t'
	return bodyLineseparator.join(snippetLines)

def GenerateSnippetJson(snippetBody, key, prefix, description):
	template = '''"#KEY#": {
	"prefix": "#PREFIX#",
	"description": "#DESCRIPTION#",
	"body": [
		#TOKEN#
	]
},'''

	template = template.replace('#TOKEN#', snippetBody)
	template = template.replace('#KEY#', key)
	template = template.replace('#PREFIX#', prefix)
	template = template.replace('#DESCRIPTION#', description)
	return template

def GenerateSnippet(content, endOfLineSequence, tabSize, key, prefix, description):
	lines = SplitContentIntoLines(content, endOfLineSequence)

	snippetLines = GenerateSnippetLines(lines, tabSize)

	body = BuildSnippetBody(snippetLines)

	snippetJson = GenerateSnippetJson(body, key, prefix, description)

	return snippetJson