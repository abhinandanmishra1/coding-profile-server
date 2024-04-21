from fastapi import APIRouter, HTTPException
from ..controllers import LeetCodeController

lc_router = APIRouter(
    prefix="/leetcode",
    tags=["leetcode"],
    responses={404: {"description": "Not found"}},
)


@lc_router.get("/{username}/info")
async def leetcode(username: str):
    try:
        lc_controller = LeetCodeController(username=username)
        user_info = await lc_controller.get_user_info()
        if user_info is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user_info
    except HTTPException as e:
        raise e


@lc_router.get("/{username}/stats")
async def leetcode(username: str):
    try:
        lc_controller = LeetCodeController(username=username)
        stats = await lc_controller.get_language_stats()
        if stats is None:
            raise HTTPException(status_code=404, detail="User not found")
        return stats
    except HTTPException as e:
        raise e


@lc_router.get("/{username}/tags")
async def leetcode(username: str):
    try:
        lc_controller = LeetCodeController(username=username)
        stats = await lc_controller.get_tag_problem_counts()
        if stats is None:
            raise HTTPException(status_code=404, detail="User not found")
        return stats
    except HTTPException as e:
        raise e


@lc_router.get("/{username}/rating")
async def leetcode(username: str):
    try:
        lc_controller = LeetCodeController(username=username)
        stats = await lc_controller.get_user_contest_rating_info()
        if stats is None:
            raise HTTPException(status_code=404, detail="User not found")
        return stats
    except HTTPException as e:
        raise e


@lc_router.get("/{username}/histogram")
async def leetcode(username: str):
    try:
        lc_controller = LeetCodeController(username=username)
        stats = await lc_controller.get_user_contest_rating_histogram()
        if stats is None:
            raise HTTPException(status_code=404, detail="User not found")
        return stats
    except HTTPException as e:
        raise e


@lc_router.get("/{username}/solved")
async def leetcode(username: str):
    try:
        lc_controller = LeetCodeController(username=username)
        stats = await lc_controller.get_user_problems_solved_info()
        if stats is None:
            raise HTTPException(status_code=404, detail="User not found")
        return stats
    except HTTPException as e:
        raise e


@lc_router.get("/{username}/badges")
async def leetcode(username: str):
    try:
        lc_controller = LeetCodeController(username=username)
        stats = await lc_controller.get_user_badges_info()
        if stats is None:
            raise HTTPException(status_code=404, detail="User not found")
        return stats
    except HTTPException as e:
        raise e


@lc_router.get("/{username}/submissions")
async def leetcode(username: str):
    try:
        lc_controller = LeetCodeController(username=username)
        stats = await lc_controller.get_user_recent_ac_submissions()
        if stats is None:
            raise HTTPException(status_code=404, detail="User not found")
        return stats
    except HTTPException as e:
        raise e


@lc_router.get("/{username}/discussions")
async def leetcode(username: str):
    try:
        lc_controller = LeetCodeController(username=username)
        stats = await lc_controller.get_user_discussion_solutions()
        if stats is None:
            raise HTTPException(status_code=404, detail="User not found")
        return stats["userSolutionTopics"]
    except HTTPException as e:
        raise e


# check if calendar data is correct or not
# maybe we need date range here
@lc_router.get("/{username}/calendar")
async def leetcode(username: str, year: str):
    print(year)
    try:
        lc_controller = LeetCodeController(username=username)
        stats = await lc_controller.get_user_profile_calendar(year=year)
        if stats is None:
            raise HTTPException(status_code=404, detail="User not found")
        return stats["matchedUser"]
    except HTTPException as e:
        raise e
