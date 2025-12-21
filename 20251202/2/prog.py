import sys
import asyncio
import random

async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()

    i, j, k = start, middle, start
    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]
            i += 1
        else:
            A2[k] = A1[j]
            j += 1
        k += 1

    while i < middle:
        A2[k] = A1[i]
        i += 1
        k += 1
    while j < finish:
        A2[k] = A1[j]
        j += 1
        k += 1

    event_out.set()

async def mtasks(A):
    N = len(A)
    B = [None for _ in range(N)]
    cur = A[:]
    next = B

    all_tasks = []
    events = [asyncio.Event() for _ in range(N)]
    for event in events:
        event.set()

    step = 1
    while step < N:
        new_events = []
        for i in range(0, N, 2*step):
            s, m, f = i, min(i+step,N), min(i+2*step,N)
            e1 = events[i//step]
            e2 = events[min(i//step+1, len(events)-1)]
            e_out = asyncio.Event()
            all_tasks.append(asyncio.create_task(
                merge(cur, next, s, m, f, e1, e2, e_out)
            ))
            new_events.append(e_out)

        cur, next = next, cur
        events = new_events
        step *= 2

    return all_tasks, cur

exec(sys.stdin.read())