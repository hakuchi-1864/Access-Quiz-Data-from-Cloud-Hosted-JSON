import json
import requests

def download_and_parse_data(url):
  """Downloads JSON data from the URL and returns a dictionary."""
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error downloading data: {response.status_code}")
    return None
# Replace with the actual structure of your downloaded data
data = download_and_parse_data("https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json?utm_source=substack&utm_medium=email")
# Print the downloaded data
print(data)

def get_correct_answer(question_id):
  for quiz in data["quizzes"]:
      for question in quiz["questions"]:
          if question["id"] == question_id:
              for choice, is_correct in question["choices"].items():
                  if is_correct:
                      return choice
  return "Question ID not found"

if __name__ == "__main__":
  question_id = int(input("Enter the Question ID: "))
  correct_answer = get_correct_answer(question_id)
  print(f"The correct answer is: {correct_answer}")










