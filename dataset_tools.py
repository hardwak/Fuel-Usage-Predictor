def filter_by_year(dataset, start_year, end_year):
    if start_year > end_year:
        raise ValueError('start_year must be less than end_year')

    filtered_dataset = (dataset[
                            (dataset['Year'] >= start_year) &
                            (dataset['Year'] <= end_year)
                            ]
                        .reset_index()
                        .drop('index', axis=1))

    return filtered_dataset
