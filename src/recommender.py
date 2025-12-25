import pandas as pd

def get_hotel_recommendations(
    data: pd.DataFrame,
    cosine_sim,
    package_type,
    start_city,
    price,
    destination
):
    filtered_data = data[
        (data['Package Type'] == package_type) &
        (data['Start City'] == start_city) &
        (data['Price Per Two Persons'] <= price) &
        (data['Destination'] == destination)
    ]

    if filtered_data.empty:
        return None

    hotel_indices = filtered_data.index
    avg_similarity_scores = [
        cosine_sim[idx].mean() for idx in hotel_indices
    ]

    result = pd.DataFrame({
        'Uniq Id': filtered_data['Uniq Id'],
        'Hotel Details': filtered_data['Hotel Details'],
        'Similarity Score': avg_similarity_scores
    })

    return result.sort_values(by='Similarity Score', ascending=False)
