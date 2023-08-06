from modules.ui.page_object.tracking_page_np import TrackingPage
import pytest
import time


@pytest.mark.ui 
def test_check_correct_cargo_number():
    tracking_page_np = TrackingPage()

    tracking_page_np.go_to()

    tracking_page_np.search_cargo("20 4507 4866 4178")

    time.sleep(5)
    tracking_page_np.close()



@pytest.mark.ui 
def test_check_incorrect_cargo_number():
    tracking_page_np = TrackingPage()

    tracking_page_np.go_to()

    tracking_page_np.search_cargo("gdkhgkthnjcfdk")

    time.sleep(5)
    tracking_page_np.close()


