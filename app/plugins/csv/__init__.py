import logging
import os
from app.commands import Command
import pandas as pd
from utils.history import get_history

class CsvCommand(Command):

    def execute(self, operation, *args):
        data_dir = './data'
        csv_file_path = os.path.join(data_dir, 'history.csv')

        # Ensure the 'data' directory exists and is writable
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' was created")

        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable.")
            return

        if operation == 'load':
            self.load_history(csv_file_path)
        elif operation == 'save':
            self.save_history(csv_file_path)
        elif operation == 'clear':
            self.clear_history(csv_file_path)
        elif operation == 'delete':
            self.delete_history(csv_file_path)
        else:
            logging.error("Unknown operation specified.")

    def load_history(self, csv_file_path):
        if os.path.exists(csv_file_path):
            df = pd.read_csv(csv_file_path)
            print("Loaded history:")
            print(df)
            logging.info("History loaded successfully.")
        else:
            logging.warning("No history found to load.")

    def save_history(self, csv_file_path):
        history = get_history()
        if not history:
            logging.error("No data provided to save.")
            return

        df = pd.DataFrame(history, columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        df.to_csv(csv_file_path, mode='w', header=True, index=False)
        logging.info(f"History saved to CSV at '{csv_file_path}'.")
        print(f"History saved to CSV at '{csv_file_path}'.")

    def clear_history(self, csv_file_path):
        if os.path.exists(csv_file_path):
            open(csv_file_path, 'w').close()  # Clear the file contents
            logging.info("History cleared.")
        else:
            logging.warning("No history found to clear.")

    def delete_history(self, csv_file_path):
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)
            logging.info(f"History file '{csv_file_path}' deleted.")
        else:
            logging.warning("No history file found to delete.")

    '''class CsvCommand(Command):
        def execute(self):
            
            # Existing code for demonstrating data structures and saving CSV...

            # Ensure the 'data' directory exists and is writable
            data_dir = './data'
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
                logging.info(f"The directory '{data_dir}' is created")

            elif not os.access(data_dir, os.W_OK):
                logging.error(f"The directory '{data_dir}' is not writable.")
                return
            
            # Convert dictionary to DataFrame and save to CSV
            states_abbreviations = {
                'CA': 'California',
                'NJ': 'New Jersey',
                'TX': 'Texas',
                'FL': 'Florida',
                'IL': 'Illinois',
                'NY': 'New York'  # Newly added state
            }
            df_states = pd.DataFrame(list(states_abbreviations.items()), columns=['Abbreviation', 'State'])
            csv_file_path = os.path.join(data_dir, 'states.csv')
            df_states.to_csv(csv_file_path, index=False)
            
            logging.info(f"States saved to CSV at '{csv_file_path}'.")
            # This is creating the path for saving the file.
            csv_file_path = os.path.join(data_dir, 'gpt_states.csv')
            logging.info(f'the relative path  to save my file is {csv_file_path}')
            # Read the CSV file back into a DataFrame
            absolute_path = os.path.abspath(csv_file_path)
            logging.info(f'the absolute path  to save my file is {absolute_path}')
            df_read_states = pd.read_csv(csv_file_path)
            
            # Print and log each state nicely
            print("States from CSV:")
            for index, row in df_read_states.iterrows():
                # First, print and log the complete record for the state
                state_info = f"{row['State Abbreviation']}: {row['State Name']}"
                print(f"Record {index}: {state_info}")
                logging.info(f"Record {index}: {state_info}")
                
                # Then, iterate through each field in the row to print and log
                for field in row.index:
                    field_info = f"    {field}: {row[field]}"
                    print(field_info)
                    logging.info(f"Index: {index}, {field_info}")'''