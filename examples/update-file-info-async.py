import nautilus
import gobject

class UpdateFileInfoAsync(nautilus.InfoProvider):
    def __init__(self):
        pass
    
    def update_file_info_full(self, provider, handle, closure, file):
        print "update_file_info_full"
        gobject.timeout_add_seconds(3, self.update_cb, provider, handle, closure)
        return nautilus.OPERATION_IN_PROGRESS
        
    def update_cb(self, provider, handle, closure):
        print "update_cb"
        self.update_complete_invoke(closure, provider, handle, result=nautilus.OPERATION_FAILED)
