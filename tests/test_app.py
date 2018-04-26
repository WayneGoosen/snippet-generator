import unittest
from app.common.GenerateSnippet import SplitContentIntoLines,EscapeDoubleQuotes \
,ReplaceSpacesWithTabDelimiter,AddDoubleQuotes,GenerateSnippetLines, \
BuildSnippetBody,GenerateSnippetJson

class TestLineSplit(unittest.TestCase):
	def setUp(self):
		self.endOfLineSequences = {"CR" : "\r", "LF": "\n", "CRLF" : "\r\n"}	

	def coreTest(self, endOfLineSequence):
		endOfLineChar = self.endOfLineSequences[endOfLineSequence]
		content = "firstline" + str(endOfLineChar) + "secondline"
		lines = SplitContentIntoLines(content, endOfLineChar)
		self.assertEqual(len(lines),2)
		self.assertEqual("firstline",lines[0])
		self.assertEqual("secondline",lines[1])

	def test_SplitContentIntoLines_cr(self):
		self.coreTest("CR")
	
	def test_SplitContentIntoLines_lf(self):
		self.coreTest("LF")
	
	def test_SplitContentIntoLines_crlf(self):
		self.coreTest("CRLF")

class TestEscapeQuotes(unittest.TestCase):
	def test_EscapeDoubleQuotes_single(self):
		quotes = '"'
		self.assertEqual(EscapeDoubleQuotes(quotes),'\\"')
	
	def test_EscapeDoubleQuotes_double(self):
		quotes = '""'
		self.assertEqual(EscapeDoubleQuotes(quotes),'\\"\\"')

class TestReplaceSpacesWithTabDelimiter(unittest.TestCase):
	def test_ReplaceSpacesWithTabDelimiter_two(self):
		content = '  '
		self.assertEqual(ReplaceSpacesWithTabDelimiter(content, 2),'\\t')

	def test_ReplaceSpacesWithTabDelimiter_four(self):
		content = '    '
		self.assertEqual(ReplaceSpacesWithTabDelimiter(content, 4),'\\t')

class TestAddDoubleQuotes(unittest.TestCase):
	def test_AddDoubleQuotes(self):
		content = 'hello'
		self.assertEqual(AddDoubleQuotes(content),'"hello"')

class TestGenerateSnippetLines(unittest.TestCase):
	def test_GenerateSnippetLines_singleCodeLine(self):
		content = 'public class Hello {'
		lines = SplitContentIntoLines(content, "\r\n")
		snippetLines = GenerateSnippetLines(lines, 2)
		self.assertEqual(len(snippetLines), 1)
		self.assertEqual(snippetLines[0],'"public class Hello {"')

	def test_GenerateSnippetLines_propertyCode(self):
		content = '''busy: {
    type: Boolean,
    value: false,
    notify: true
}'''
		lines = SplitContentIntoLines(content, "\n")
		snippetLines = GenerateSnippetLines(lines, 4)
		self.assertEqual(len(snippetLines), 5)
		self.assertEqual(snippetLines[0],'"busy: {"')
		self.assertEqual(snippetLines[1],'"\\ttype: Boolean,"')
		self.assertEqual(snippetLines[2],'"\\tvalue: false,"')
		self.assertEqual(snippetLines[3],'"\\tnotify: true"')
		self.assertEqual(snippetLines[4],'"}"')

	def test_GenerateSnippetLines_ensureEscapeDoubleQuotes(self):
		content = '<paper-dialog id="dialog" modal>'
		lines = SplitContentIntoLines(content, "\n")
		snippetLines = GenerateSnippetLines(lines, 2)
		self.assertEqual(len(snippetLines), 1)
		self.assertEqual(snippetLines[0],'"<paper-dialog id=\\"dialog\\" modal>"')

class TestBuildSnippetBody(unittest.TestCase):
    def test_BuildSnippetBody(self):
        content = '''busy: {
    type: Boolean,'''
        lines = SplitContentIntoLines(content, "\n")
        snippetLines = GenerateSnippetLines(lines, 4)
        snippetBody = BuildSnippetBody(snippetLines)
        self.assertEqual(snippetBody, '"busy: {",\n\t\t"\\ttype: Boolean,"')

class TestGenerateSnippetJson(unittest.TestCase):
    def test_GenerateSnippetJson(self):
        content = 'public class Hello {'
        lines = SplitContentIntoLines(content, "\n")
        snippetLines = GenerateSnippetLines(lines, 4)
        snippetBody = BuildSnippetBody(snippetLines)
        snippetJson = GenerateSnippetJson(snippetBody,'','','')
        self.assertEqual(snippetJson, '"": {\n\t"prefix": "",\n\t"description": "",\n\t"body": [\n\t\t"public class Hello {"\n\t]\n},')

if __name__ == '__main__':
    unittest.main()