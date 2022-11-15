import pandas as pd

from src.utils import get_matrix_binary


def test_get_matrix_binary1(short_data: pd.DataFrame):
    # arrange
    initial_list = ['India', 'South Africa']
    initial_data = short_data['country']
    # action
    actual = get_matrix_binary(data=initial_data, list_flattened=initial_list)
    # assert
    expected_df = pd.DataFrame([[0, 1], [1, 0]]).astype(float)
    expected_shape = (2, 2)
    assert expected_shape == actual.shape
    assert actual.eq(expected_df).all().all()
