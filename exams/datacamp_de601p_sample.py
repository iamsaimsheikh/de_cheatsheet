import pandas as pd
import numpy as np

def all_pet_data(pet_csv, health_csv, users_csv):
    # Load files
    pet_df = pd.read_csv(pet_csv, parse_dates=['date'])
    health_df = pd.read_csv(health_csv, parse_dates=['visit_date'])
    users_df = pd.read_csv(users_csv)

    # Drop missing critical values
    pet_df = pet_df.dropna(subset=['pet_id', 'date'])
    health_df = health_df.dropna(subset=['pet_id', 'visit_date'])
    users_df = users_df.dropna(subset=['owner_id'])

    # Clean pet_df
    pet_df['activity_type'] = pet_df['activity_type'].str.strip()
    pet_df['activity_type'] = pet_df['activity_type'].replace({
        "Play": "Playing",
        "Walk": "Walking",
        "Rest": "Resting"
    })
    pet_df['issue'] = np.nan
    pet_df['resolution'] = np.nan

    # Clean health_df
    health_df = health_df.rename(columns={'visit_date': 'date'})
    health_df['activity_type'] = 'Health'
    health_df['duration_minutes'] = 0
    health_df['issue'] = health_df['issue'].str.strip()
    health_df['resolution'] = health_df['resolution'].str.strip()

    # Clean users_df
    users_df['owner_age_group'] = users_df['owner_age_group'].str.strip()
    users_df['pet_type'] = users_df['pet_type'].str.strip()

    # Combine pet and health activities
    combined_df = pd.concat([pet_df, health_df], ignore_index=True)

    # Merge with user info
    final_df = combined_df.merge(users_df, on='pet_id', how='left')

    # Replace '-' and convert to float
    final_df['duration_minutes'] = final_df['duration_minutes'].replace('-', np.nan).astype(float)

    # Return final cleaned DataFrame
    return final_df