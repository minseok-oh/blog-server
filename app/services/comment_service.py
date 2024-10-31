from app.schemas.comment import Comment


def update_comment(comment: Comment) -> Comment:
    """
    댓글을 수정합니다.
    TODO: Controller에서 호출 시에는 comment_id를 인자로 받아서 해당 댓글을 조회한 후에 댓글을 수정합니다.
    TODO: 추후에 content를 인자로 받아서 댓글을 수정할 수 있도록 수정합니다.
    """
    return comment.update_comment_date()
