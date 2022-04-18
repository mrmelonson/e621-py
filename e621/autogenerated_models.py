# This file has been automagically generated by our scripts
# Please, do not edit it by hand because all of your changes
# will inevitably be overwritten. Edit models.py instead.

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import Field

from .base_model import BaseModel

__all__ = (
    "File",
    "Preview",
    "Field720p",
    "Field480p",
    "Original",
    "Alternates",
    "Sample",
    "Score",
    "Tags",
    "Flags",
    "Relationships",
    "Post",
    "Posts",
    "PostFlag",
    "Tag",
    "TagAlias",
    "Note",
    "Pool",
    "User",
    "PostVersion",
    "PostApproval",
    "NoteVersion",
    "WikiPage",
    "WikiPageVersion",
    "Url",
    "Artist",
    "ArtistVersion",
    "TagTypeVersion",
    "TagImplication",
    "BulkUpdateRequest",
    "Blip",
    "Takedown",
    "UserFeedback",
    "ForumTopic",
    "PostSet",
)


class File(BaseModel):
    width: int
    height: int
    ext: str
    size: int
    md5: str
    url: str


class Preview(BaseModel):
    width: int
    height: int
    url: str


class Field720p(BaseModel):
    type: str
    height: int
    width: int
    urls: List[str]


class Field480p(Field720p):
    pass


class Original(BaseModel):
    type: str
    height: int
    width: int
    urls: List[Optional[str]]


class Alternates(BaseModel):
    field_720p: Optional[Field720p] = Field(None, alias="720p")
    field_480p: Optional[Field480p] = Field(None, alias="480p")
    original: Optional[Original] = None


class Sample(BaseModel):
    has: bool
    height: int
    width: int
    url: str
    alternates: Alternates


class Score(BaseModel):
    up: int
    down: int
    total: int


class Tags(BaseModel):
    general: List[str]
    species: List[str]
    character: List[str]
    copyright: List[str]
    artist: List[str]
    invalid: List[str]
    lore: List[str]
    meta: List[str]


class Flags(BaseModel):
    pending: bool
    flagged: bool
    note_locked: bool
    status_locked: bool
    rating_locked: bool
    deleted: bool


class Relationships(BaseModel):
    parent_id: Optional[int]
    has_children: bool
    has_active_children: bool
    children: List[int]


class Post(BaseModel):
    id: int
    created_at: str
    updated_at: str
    file: Optional[File]
    preview: Optional[Preview]
    sample: Optional[Sample]
    score: Score
    tags: Tags
    locked_tags: List[str]
    change_seq: int
    flags: Flags
    rating: str
    fav_count: int
    sources: List[str]
    pools: List[int]
    relationships: Relationships
    approver_id: Optional[int]
    uploader_id: int
    description: str
    comment_count: int
    is_favorited: bool
    has_notes: bool
    duration: Optional[float]


class Posts(BaseModel):
    posts: List[Post]


class PostFlag(BaseModel):
    id: int
    created_at: str
    post_id: int
    reason: str
    is_resolved: bool
    updated_at: str
    is_deletion: bool
    category: str
    creator_id: Optional[int] = None


class Tag(BaseModel):
    id: int
    name: str
    post_count: int
    related_tags: str
    related_tags_updated_at: str
    category: int
    is_locked: bool
    created_at: str
    updated_at: str


class TagAlias(BaseModel):
    id: int
    antecedent_name: str
    reason: str
    creator_id: int
    created_at: str
    forum_post_id: Optional[int]
    updated_at: Optional[str]
    forum_topic_id: Optional[int]
    consequent_name: str
    status: str
    post_count: int
    approver_id: Optional[int]


class Note(BaseModel):
    id: int
    created_at: str
    updated_at: str
    creator_id: int
    x: int
    y: int
    width: int
    height: int
    version: int
    is_active: bool
    post_id: int
    body: str
    creator_name: str


class Pool(BaseModel):
    id: int
    name: str
    created_at: str
    updated_at: str
    creator_id: int
    description: str
    is_active: bool
    category: str
    is_deleted: bool
    post_ids: List[int]
    creator_name: str
    post_count: int


class User(BaseModel):
    id: int
    created_at: str
    name: str
    level: int
    base_upload_limit: int
    post_upload_count: int
    post_update_count: int
    note_update_count: int
    is_banned: bool
    can_approve_posts: bool
    can_upload_free: bool
    level_string: str
    avatar_id: Optional[int]


class PostVersion(BaseModel):
    id: int
    post_id: int
    tags: str
    updater_id: int
    updated_at: str
    rating: str
    parent_id: Optional[int]
    source: str
    description: str
    reason: Optional[str]
    locked_tags: Optional[str]
    added_tags: List[str]
    removed_tags: List[str]
    added_locked_tags: List[str]
    removed_locked_tags: List[str]
    rating_changed: bool
    parent_changed: bool
    source_changed: bool
    description_changed: bool
    version: int
    obsolete_added_tags: str
    obsolete_removed_tags: str
    unchanged_tags: str
    updater_name: str


class PostApproval(BaseModel):
    id: int
    user_id: int
    post_id: int
    created_at: str
    updated_at: str


class NoteVersion(BaseModel):
    id: int
    created_at: str
    updated_at: str
    x: int
    y: int
    width: int
    height: int
    body: str
    version: int
    is_active: bool
    note_id: int
    post_id: int
    updater_id: int


class WikiPage(BaseModel):
    id: int
    created_at: str
    updated_at: str
    title: str
    body: str
    creator_id: int
    is_locked: bool
    updater_id: int
    is_deleted: bool
    other_names: List[str]
    creator_name: str
    category_name: int


class WikiPageVersion(BaseModel):
    id: int
    created_at: str
    updated_at: str
    title: str
    body: str
    updater_id: int
    wiki_page_id: int
    is_locked: bool
    other_names: List[str]
    is_deleted: bool
    reason: Optional[str]


class Url(BaseModel):
    id: int
    artist_id: int
    url: str
    normalized_url: str
    created_at: str
    updated_at: str
    is_active: bool


class Artist(BaseModel):
    id: int
    name: str
    updated_at: str
    is_active: bool
    other_names: List[str]
    group_name: str
    linked_user_id: Optional[int]
    created_at: str
    is_banned: bool
    creator_id: int
    is_locked: bool
    notes: Optional[str]
    urls: List[Url]


class ArtistVersion(BaseModel):
    id: int
    artist_id: int
    name: str
    updater_id: int
    created_at: str
    updated_at: str
    is_active: bool
    other_names: List[str]
    group_name: str
    is_banned: bool
    notes_changed: bool
    urls: List[str]


class TagTypeVersion(BaseModel):
    id: int
    created_at: str
    updated_at: str
    old_type: int
    new_type: int
    is_locked: bool
    tag_id: int
    creator_id: int


class TagImplication(BaseModel):
    id: int
    reason: str
    creator_id: int
    created_at: str
    forum_post_id: int
    antecedent_name: str
    consequent_name: str
    status: str
    forum_topic_id: int
    updated_at: Optional[str]
    descendant_names: List[str]
    approver_id: Optional[int]


class BulkUpdateRequest(BaseModel):
    id: int
    user_id: int
    forum_topic_id: int
    script: str
    status: str
    created_at: str
    updated_at: str
    approver_id: Optional[int]
    forum_post_id: Optional[int]
    title: str


class Blip(BaseModel):
    id: int
    creator_id: int
    body: str
    response_to: Optional[int]
    created_at: str
    updated_at: str
    is_hidden: bool
    warning_type: Any  # ? What is this
    warning_user_id: Optional[int]
    creator_name: str


class Takedown(BaseModel):
    id: int
    status: str
    approver_id: Optional[int]
    reason_hidden: bool
    created_at: str
    updated_at: str
    post_count: int


class UserFeedback(BaseModel):
    id: int
    user_id: int
    creator_id: int
    created_at: str
    body: str
    category: str
    updated_at: str


class ForumTopic(BaseModel):
    id: int
    creator_id: int
    updater_id: int
    title: str
    response_count: int
    is_sticky: bool
    is_locked: bool
    is_hidden: bool
    created_at: str
    updated_at: str
    category_id: int
    min_level: int


class ForumPost(BaseModel):
    id: int
    created_at: str
    updated_at: str
    body: str
    creator_id: int
    updater_id: int
    topic_id: int
    is_hidden: bool
    warning_type: Any
    warning_user_id: Optional[int]


class PostSet(BaseModel):
    id: int
    created_at: str
    updated_at: str
    creator_id: int
    is_public: bool
    name: str
    shortname: str
    description: str
    post_count: int
    transfer_on_delete: bool
    post_ids: List[int]


__all__ = (
    "File",
    "Preview",
    "Field720p",
    "Field480p",
    "Original",
    "Alternates",
    "Sample",
    "Score",
    "Tags",
    "Flags",
    "Relationships",
    "Post",
    "Posts",
    "PostFlag",
    "Tag",
    "TagAlias",
    "Note",
    "Pool",
    "User",
    "PostVersion",
    "PostApproval",
    "NoteVersion",
    "WikiPage",
    "WikiPageVersion",
    "Url",
    "Artist",
    "ArtistVersion",
    "TagTypeVersion",
    "TagImplication",
    "BulkUpdateRequest",
    "Blip",
    "Takedown",
    "UserFeedback",
    "ForumTopic",
    "ForumPost",
    "PostSet",
)
