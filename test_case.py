import pytest
from SystemDriveFinder import SystemDriveFinder
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['c','D']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=Filesearcher()
        d=obj.search_for_file('d','demo.html')
        self.expected_filename=d[0]
        self.actual_res='d:\jose\demo.html'
        assert.self.expected_filename=self.actual_res