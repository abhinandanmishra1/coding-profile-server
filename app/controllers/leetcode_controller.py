import requests
from ..helpers import (
    get_lc_options,
) 


class LeetCodeController:
    def __init__(self, username):
        self.username = username

    async def get_user_info(self):
        options = get_lc_options("userInfo", self.username)
        response = requests.get(
            options["url"], headers=options["headers"], data=options["body"]
        )

        if response.status_code == 200:
            result = response.json()
            return result["data"]["matchedUser"]
        else:
            return None

    async def get_language_stats(self):
        options = get_lc_options("languageStats", self.username)
        response = requests.get(
            options["url"], headers=options["headers"], data=options["body"]
        )

        if response.status_code == 200:
            result = response.json()
            return result["data"]["matchedUser"]["languageProblemCount"]
        else:
            return None

    async def get_tag_problem_counts(self):
        options = get_lc_options("tagProblemCounts", self.username)
        response = requests.get(
            options["url"], headers=options["headers"], data=options["body"]
        )

        if response.status_code == 200:
            result = response.json()
            return result["data"]["matchedUser"]["tagProblemCounts"]
        else:
            return None

    async def get_user_contest_rating_info(self):
        options = get_lc_options("userContestRatingInfo", self.username)
        response = requests.get(
            options["url"], headers=options["headers"], data=options["body"]
        )

        if response.status_code == 200:
            result = response.json()
            return result["data"]
        else:
            return None

    async def get_user_contest_rating_histogram(self):
        options = get_lc_options("userContestRatingHistogram", self.username)
        response = requests.get(
            options["url"], headers=options["headers"], data=options["body"]
        )

        if response.status_code == 200:
            result = response.json()
            return result
        else:
            return None

    async def get_user_problems_solved_info(self):
        options = get_lc_options("userProblemsSolvedInfo", self.username)
        response = requests.get(
            options["url"], headers=options["headers"], data=options["body"]
        )

        if response.status_code == 200:
            result = response.json()
            all_questions_count = result["data"]["allQuestionsCount"]
            problems_solved_beats_stats = result["data"]["matchedUser"][
                "problemsSolvedBeatsStats"
            ]
            solved_problems_count = result["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]
            result = {}
            result["All"] = {}
            for problem in problems_solved_beats_stats:
                result[problem["difficulty"]] = problem
            
            for problem in solved_problems_count:
                result[problem["difficulty"]]["solvedCount"] = problem["count"]
            
            for problem in all_questions_count:
                result[problem["difficulty"]]["totalCount"] = problem["count"]

            return result
        else:
            return None

    async def get_user_badges_info(self):
        options = get_lc_options("userBadgesInfo", self.username)
        response = requests.get(
            options["url"], headers=options["headers"], data=options["body"]
        )

        if response.status_code == 200:
            result = response.json()
            return result["data"]["matchedUser"]["badges"]
        else:
            return None

    async def get_user_recent_ac_submissions(self):
        options = get_lc_options(
            "userRecentAcSubmissions", self.username, alt_options={"limit": 20}
        )
        response = requests.get(
            options["url"], headers=options["headers"], data=options["body"]
        )

        if response.status_code == 200:
            result = response.json()
            return result["data"]
        else:
            return None

    async def get_user_discussion_solutions(self):
        options = get_lc_options("userDiscussionSolutions", self.username)
        response = requests.get(
            options["url"], headers=options["headers"], data=options["body"]
        )

        if response.status_code == 200:
            result = response.json()
            return result["data"]
        else:
            return None

    async def get_user_profile_calendar(self):
        options = get_lc_options("userProfileCalendar", self.username)
        response = requests.get(
            options["url"], headers=options["headers"], data=options["body"]
        )

        if response.status_code == 200:
            result = response.json()
            return result["data"]
        else:
            return None
