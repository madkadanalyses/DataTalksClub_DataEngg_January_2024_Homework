import re
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    print(f"Preprocessing: rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing: rows with zero trip distance: {data['trip_distance'].isin([0]).sum()}")

    def camel_to_snake(column_name):
        column_name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', column_name).lower()

    data.rename(columns=lambda x: camel_to_snake(x), inplace=True)
    data["lpep_pickup_date"] = data["lpep_pickup_datetime"].dt.date

    return data[(data['passenger_count']>0) & (data['trip_distance']>0)]


@test
def test_output_1(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

@test
def test_output_2(output, *args) -> None:
    assert "vendor_id" in output.columns, "Camel case is not converted to snake case"

@test
def test_output_3(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, "There are rides with zero passengers"

@test
def test_output_4(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum() == 0, "There are rides with zero trip distance"