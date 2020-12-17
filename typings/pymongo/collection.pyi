from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple, Union

from bson.codec_options import CodecOptions
from pymongo.bulk import BulkOperationBuilder
from pymongo.change_stream import CollectionChangeStream
from pymongo.client_session import ClientSession
from pymongo.collation import Collation
from pymongo.command_cursor import CommandCursor
from pymongo.common import BaseObject
from pymongo.cursor import Cursor, CursorType, RawBatchCursor
from pymongo.database import Database
from pymongo.operations import (
    DeleteMany,
    DeleteOne,
    IndexModel,
    InsertOne,
    ReplaceOne,
    UpdateMany,
    UpdateOne,
)
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import ReadPreference
from pymongo.results import (
    BulkWriteResult,
    DeleteResult,
    InsertManyResult,
    InsertOneResult,
    UpdateResult,
)
from pymongo.write_concern import WriteConcern
from typing_extensions import Literal, TypedDict

class ReturnDocument:
    BEFORE: Literal[False] = False
    AFTER: Literal[True] = True

class _ResumeToken(TypedDict):
    _data: bytes

class Collection(BaseObject):
    @property
    def full_name(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def database(self) -> Database: ...
    def with_options(
        self,
        codec_options: Optional[CodecOptions] = ...,
        read_preference: Optional[ReadPreference] = ...,
        write_concern: Optional[WriteConcern] = ...,
        read_concern: Optional[ReadConcern] = ...,
    ) -> Collection: ...
    def bulk_write(
        self,
        requests: Sequence[
            Union[InsertOne, UpdateOne, UpdateMany, ReplaceOne, DeleteOne, DeleteMany]
        ],
        ordered: bool = ...,
        bypass_document_validation: bool = ...,
        session: Optional[ClientSession] = ...,
    ) -> BulkWriteResult: ...
    def insert_one(
        self,
        document: Dict[str, Any],
        bypass_document_validation: bool = ...,
        session: Optional[ClientSession] = ...,
    ) -> InsertOneResult: ...
    def insert_many(
        self,
        documents: Iterable[Dict[str, Any]],
        ordered: bool = ...,
        bypass_document_validation: bool = ...,
        session: Optional[ClientSession] = ...,
    ) -> InsertManyResult: ...
    def replace_one(
        self,
        filter: Dict[str, Any],
        replacement: Dict[str, Any],
        bypass_document_validation: bool = ...,
        collation: Optional[Collation] = ...,
        hint: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
    ) -> UpdateResult: ...
    def update_one(
        self,
        filter: Dict[str, Any],
        update: Dict[str, Any],
        upsert: bool = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Collation] = ...,
        array_filters: Optional[List[Dict[str, Any]]] = ...,
        session: Optional[ClientSession] = ...,
    ) -> UpdateResult: ...
    def update_many(
        self,
        filter: Dict[str, Any],
        update: Dict[str, Any],
        upsert: bool = ...,
        array_filters: Optional[List[Dict[str, Any]]] = ...,
        bypass_document_validation: bool = ...,
        collation: Optional[Collation] = ...,
        hint: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
    ) -> UpdateResult: ...
    def delete_one(
        self,
        filter: Dict[str, Any],
        collation: Optional[Collation] = ...,
        hint: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
    ) -> DeleteResult: ...
    def delete_many(
        self,
        filter: Dict[str, Any],
        collation: Optional[Collation] = ...,
        hint: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
    ) -> DeleteResult: ...
    def aggregate(
        self,
        pipeline: List[Dict[str, Any]],
        session: Optional[ClientSession] = ...,
        allowDiskUse: bool = ...,
        maxTimeMS: int = ...,
        batchSize: int = ...,
        collation: Optional[Collation] = ...,
        useCursor: bool = ...,
    ) -> CommandCursor: ...
    def aggregate_raw_batches(
        self,
        pipeline: List[Dict[str, Any]],
        session: Optional[ClientSession] = ...,
        allowDiskUse: bool = ...,
        maxTimeMS: int = ...,
        batchSize: int = ...,
        collation: Optional[Collation] = ...,
        useCursor: bool = ...,
    ) -> RawBatchCursor: ...
    def watch(
        self,
        pipeline: Optional[List[Dict[str, Any]]] = ...,
        full_document: Optional[Literal["updateLookup"]] = ...,
        resume_after: Optional[_ResumeToken] = ...,
        max_await_time_ms: Optional[int] = ...,
        batch_size: Optional[int] = ...,
        collation: Optional[Collation] = ...,
        session: Optional[ClientSession] = ...,
        start_after: Optional[_ResumeToken] = ...,
    ) -> CollectionChangeStream: ...
    def find(
        self,
        filter: Optional[Dict[str, Any]] = ...,
        projection: Optional[Dict[str, Any]] = ...,
        skip: int = ...,
        limit: int = ...,
        no_cursor_timeout: bool = ...,
        cursor_type: CursorType = ...,
        sort: List[Tuple[str, Union[int, Dict[str, str]]]] = ...,
        allow_partial_results: bool = ...,
        oplog_replay: bool = ...,
        modifiers: Dict[str, Any] = ...,
        batch_size: int = ...,
        manipulate: bool = ...,
        collation: Optional[Collation] = ...,
        hint: Optional[Dict[str, int]] = ...,
        max_scan: Optional[int] = ...,
        max_time_ms: Optional[int] = ...,
        max: Optional[List[Tuple[str, int]]] = ...,
        min: Optional[List[Tuple[str, int]]] = ...,
        return_key: bool = ...,
        show_record_id: bool = ...,
        snapshot: bool = ...,
        comment: Optional[str] = ...,
        session: Optional[ClientSession] = ...,
    ) -> Cursor: ...
    def find_raw_batches(
        self,
        filter: Optional[Dict[str, Any]] = ...,
        projection: Optional[Dict[str, Any]] = ...,
        skip: int = ...,
        limit: int = ...,
        no_cursor_timeout: bool = ...,
        cursor_type: CursorType = ...,
        sort: List[Tuple[str, Union[int, Dict[str, str]]]] = ...,
        allow_partial_results: bool = ...,
        oplog_replay: bool = ...,
        modifiers: Dict[str, Any] = ...,
        batch_size: int = ...,
        manipulate: bool = ...,
        collation: Optional[Collation] = ...,
        hint: Optional[Dict[str, int]] = ...,
        max_scan: Optional[int] = ...,
        max_time_ms: Optional[int] = ...,
        max: Optional[List[Tuple[str, int]]] = ...,
        min: Optional[List[Tuple[str, int]]] = ...,
        return_key: bool = ...,
        show_record_id: bool = ...,
        snapshot: bool = ...,
        comment: Optional[str] = ...,
    ) -> RawBatchCursor: ...
    def find_one(
        self,
        filter: Optional[Dict[str, Any]],
        projection: Optional[Dict[str, Any]] = ...,
        skip: int = ...,
        limit: int = ...,
        no_cursor_timeout: bool = ...,
        cursor_type: CursorType = ...,
        sort: List[Tuple[str, Union[int, Dict[str, str]]]] = ...,
        allow_partial_results: bool = ...,
        oplog_replay: bool = ...,
        modifiers: Dict[str, Any] = ...,
        batch_size: int = ...,
        manipulate: bool = ...,
        collation: Optional[Collation] = ...,
        hint: Optional[Dict[str, int]] = ...,
        max_scan: Optional[int] = ...,
        max_time_ms: Optional[int] = ...,
        max: Optional[List[Tuple[str, int]]] = ...,
        min: Optional[List[Tuple[str, int]]] = ...,
        return_key: bool = ...,
        show_record_id: bool = ...,
        snapshot: bool = ...,
        comment: Optional[str] = ...,
        session: Optional[ClientSession] = ...,
    ) -> Optional[Dict[str, Any]]: ...
    def find_one_and_delete(
        self,
        filter: Optional[Dict[str, Any]],
        replacement: Dict[str, Any],
        projection: Optional[Dict[str, Any]] = ...,
        sort: List[Tuple[str, Union[int, Dict[str, str]]]] = ...,
        hint: Optional[Dict[str, int]] = ...,
        session: Optional[ClientSession] = ...,
    ) -> Optional[Dict[str, Any]]: ...
    def find_one_and_replace(
        self,
        filter: Optional[Dict[str, Any]],
        projection: Optional[Dict[str, Any]] = ...,
        sort: List[Tuple[str, Union[int, Dict[str, str]]]] = ...,
        return_document: ReturnDocument = ...,
        hint: Optional[Dict[str, int]] = ...,
        session: Optional[ClientSession] = ...,
    ) -> Optional[Dict[str, Any]]: ...
    def find_one_and_update(
        self,
        filter: Optional[Dict[str, Any]],
        update: Dict[str, Any],
        projection: Optional[Dict[str, Any]] = ...,
        sort: List[Tuple[str, Union[int, Dict[str, str]]]] = ...,
        return_document: ReturnDocument = ...,
        array_filters: Optional[List[Dict[str, Any]]] = ...,
        hint: Optional[Dict[str, int]] = ...,
        session: Optional[ClientSession] = ...,
    ) -> Optional[Dict[str, Any]]: ...
    def count_documents(
        self,
        filter: Dict[str, Any],
        session: Optional[ClientSession] = ...,
        skip: int = ...,
        limit: int = ...,
        collation: Collation = ...,
        hint: Union[str, List[Tuple[str, int]]] = ...,
    ) -> int: ...
    def estimated_document_count(
        self,
        maxTimeMS: int = ...,
    ) -> int: ...
    def distinct(
        self,
        key: str,
        filter: Optional[Dict[str, Any]] = ...,
        session: Optional[ClientSession] = ...,
        maxTimeMS: int = ...,
        collation: Collation = ...,
    ) -> List[Any]: ...
    def create_index(
        self,
        keys: Union[str, List[Tuple[str, int]]],
        name: Optional[str] = ...,
        unique: bool = ...,
        background: bool = ...,
        sparse: bool = ...,
        bucketSize: int = ...,
        min: int = ...,
        max: int = ...,
        expireAfterSeconds: int = ...,
        partialFilterExpression: Dict[str, Any] = ...,
        collation: Collation = ...,
        wildcardProjection: Dict[str, Any] = ...,
        hidden: bool = ...,
    ) -> List[str]: ...
    def create_indexes(
        self,
        indexes: List[IndexModel],
        session: Optional[ClientSession] = ...,
    ) -> List[str]: ...
    def drop_index(
        self,
        index_or_name: Union[str, List[str]],
        session: Optional[ClientSession] = ...,
    ) -> None: ...
    def drop_indexes(
        self,
        session: Optional[ClientSession] = ...,
    ) -> None: ...
    def reindex(
        self,
        session: Optional[ClientSession] = ...,
    ) -> None: ...
    def list_indexes(
        self,
        session: Optional[ClientSession] = ...,
    ) -> CommandCursor: ...
    def index_information(
        self,
        session: Optional[ClientSession] = ...,
    ) -> Dict[str, Any]: ...
    def drop(
        self,
        session: Optional[ClientSession] = ...,
    ) -> None: ...
    def rename(
        self,
        new_name: str,
        session: Optional[ClientSession] = ...,
        dropTarget: bool = ...,
    ) -> Any: ...
    def options(
        self,
        session: Optional[ClientSession] = ...,
    ) -> Dict[str, Any]: ...
    def map_reduce(
        self,
        map: str,
        reduce: str,
        out: Union[str, Dict[str, Any]],
        full_response: bool = ...,
        session: Optional[ClientSession] = ...,
        limit: int = ...,
    ) -> Dict[str, Any]: ...
    def inline_map_reduce(
        self,
        map: str,
        reduce: str,
        full_response: bool = ...,
        session: Optional[ClientSession] = ...,
        limit: int = ...,
    ) -> Dict[str, Any]: ...
    def parallel_scan(
        self, num_cursors: int, session: Optional[ClientSession] = ...
    ) -> List[CommandCursor]: ...
    def iniitalize_unordered_bulk_op(
        self, bypass_document_validation: bool = ...
    ) -> BulkOperationBuilder: ...
    def iniitalize_ordered_bulk_op(
        self, bypass_document_validation: bool = ...
    ) -> BulkOperationBuilder: ...
    def group(
        self,
        key: int,
        condition: Any,
        initial: Any,
        reduce: Any,
        finialize: Optional[Any] = ...,
    ) -> Any: ...
    def count(
        self,
        filter: Dict[str, Any],
        session: Optional[ClientSession] = ...,
        skip: int = ...,
        limit: int = ...,
        maxTimeMS: int = ...,
        collation: Collation = ...,
        hint: Union[str, List[Tuple[str, int]]] = ...,
    ) -> int: ...
    def insert(
        self,
        doc_or_docs: Any,
        manipulate: bool = ...,
        check_keys: bool = ...,
        continue_on_error: bool = ...,
    ) -> Any: ...
    def save(
        self, to_save: Any, manipulate: bool = ..., check_keys: bool = ...
    ) -> Any: ...
    def update(
        self,
        spec: Any,
        document: Any,
        upsert: bool = ...,
        manipulate: bool = ...,
        multi: bool = ...,
        check_keys: bool = ...,
    ) -> Any: ...
    def remove(self, spec_or_id: Optional[Any] = ..., multi: bool = ...) -> Any: ...
    def find_and_modify(
        self, spec_or_id: Optional[Any] = ..., multi: bool = ..., w: int = ...
    ) -> Any: ...
    def ensure_index(
        self, key_or_list: Union[str, List[str]], cache_for: int = ...
    ) -> Optional[str]: ...
