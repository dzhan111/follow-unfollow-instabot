# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'username'
insta_password = 'pass'

# InstaPy session
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=10,
                                    min_following=20)
    session.set_quota_supervisor(enabled=True,
                            sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                            sleepyhead=True,
                            stochastic_flow=True,
                            notify_me=True,
                            peak_likes_hourly=57,
                            peak_likes_daily=585,
                            peak_comments_hourly=21,
                            peak_comments_daily=182,
                            peak_follows_hourly=48,
                            peak_follows_daily=None,
                            peak_unfollows_hourly=35,
                            peak_unfollows_daily=402,
                            peak_server_calls_hourly=None,
                            peak_server_calls_daily=4700)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # activities

    """ Massive Follow of users followers 
    """
    session.follow_user_followers(['fus_gring', 'taco.with.lalo', 'breakingbadreel'], amount=100,
                                  randomize=False, interact=False)

    """ unfollow non followers, first in first out
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)

    """ unfollow non followers, first in first out
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)

    """ unfollow all people instapy followed after a certain time
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=601)

    """ stuff i will add engagement to
    """
    photo_comments = ['saul is here',
        'sus gus',
        'saul :thumbsup:',
        'i love breaking bad',
        'my name is saul',
        'breaking bad is best ww',
        'relax, just call saul',
        'sussy gussy',
        'when the imposter is gus',
        'hi']

    session.set_do_comment(enabled = True, percentage = 95)
    session.set_comments(photo_comments, media = 'Photo')
    session.join_pods(topic='entertainment', engagement_mode='no_comments')
