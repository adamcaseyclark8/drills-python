import asyncio
import time
from unittest.mock import AsyncMock

import pytest

from code.reimplementation.implement_promise import delay, fetch_with_retry


class TestDelay:
    def test_resolves_with_value_after_ms(self):
        assert asyncio.run(delay(50, 'hello')) == 'hello'

    def test_resolves_after_the_specified_time(self):
        start = time.monotonic()
        asyncio.run(delay(100, None))
        assert time.monotonic() - start >= 0.1


class TestFetchWithRetry:
    def test_resolves_immediately_on_first_success(self):
        fn = AsyncMock(return_value='ok')
        assert asyncio.run(fetch_with_retry(fn, 3)) == 'ok'
        assert fn.call_count == 1

    def test_retries_on_failure_and_eventually_resolves(self):
        fn = AsyncMock(side_effect=[Exception('fail'), Exception('fail'), 'ok'])
        assert asyncio.run(fetch_with_retry(fn, 3)) == 'ok'
        assert fn.call_count == 3

    def test_rejects_after_all_retries_exhausted(self):
        fn = AsyncMock(side_effect=Exception('always fails'))
        with pytest.raises(Exception, match='always fails'):
            asyncio.run(fetch_with_retry(fn, 2))
        assert fn.call_count == 3

    def test_resolves_with_0_retries_if_first_call_succeeds(self):
        fn = AsyncMock(return_value='done')
        assert asyncio.run(fetch_with_retry(fn, 0)) == 'done'

    def test_rejects_immediately_with_0_retries_on_failure(self):
        fn = AsyncMock(side_effect=Exception('nope'))
        with pytest.raises(Exception, match='nope'):
            asyncio.run(fetch_with_retry(fn, 0))
        assert fn.call_count == 1
