import os
import asyncio
from typing import Dict, List, Any
from pydantic import BaseModel, Field

# ===================================================================== #
# DOMAIN 4: DOCUMENT INTELLIGENCE & INGESTION MECHANICS (ASYNC)       #
# ===================================================================== #

class DocumentChunk(BaseModel):
    chunk_id: str
    content: str
    page_number: int
    metadata: Dict[str, Any] = Field(default_factory=dict)

class IngestionPipeline:
    """
    Simulates an Asynchronous Azure AI Document Intelligence + Azure AI Search Ingestion.
    Teaches you high-performance orchestration and high-recall chunking for the AI-103.
    """
    def __init__(self, index_name: str):
        self.index_name = index_name
        print(f"📡 Async Ingestion Pipeline initialized for Index: {self.index_name}")

    async def simulate_document_intelligence_layout(self, file_path: str) -> str:
        """
        Simulates parsing a complex document asynchronously.
        Using async prevents network and file I/O operations from stalling the engine.
        """
        print(f"📖 [Async] Starting layout semantics extraction for '{file_path}'...")
        
        # Simulate non-blocking network I/O latency (e.g., waiting on Azure endpoint response)
        await asyncio.sleep(1.0) 
        
        mock_markdown_output = (
            "# Q2 Cost Optimization Report\n\n"
            "## Vector Database Infrastructure Analysis\n"
            "| Cluster Tier | Monthly Cost | Query Latency |\n"
            "|---|---|---|\n"
            "| Standard HNSW | $450 | 14ms |\n"
            "| Premium IVF | $1,200 | 8ms |\n\n"
            "Conclusion: Shifting evaluation environments to HNSW saves 62% in overhead costs."
        )
        return mock_markdown_output

    async def chunk_document(self, text: str, chunk_size: int = 300, chunk_overlap: int = 50) -> List[DocumentChunk]:
        """
        Implements an asynchronous sliding window chunking mechanism.
        
        AI-103 Strategy: Introducing a controlled overlap ensures semantic context 
        is preserved at text boundaries, maximizing Vector Recall Accuracy during queries.
        """
        print(f"✂ [Async] Processing sliding window chunking (Size: {chunk_size}, Overlap: {chunk_overlap})...")
        
        # Yield control briefly to ensure the event loop stays unblocked
        await asyncio.sleep(0.01)
        
        chunks = []
        start_idx = 0
        text_length = len(text)
        chunk_count = 0

        while start_idx < text_length:
            end_idx = min(start_idx + chunk_size, text_length)
            
            # Smart word-boundary snapping to avoid cutting words in half
            if end_idx < text_length:
                next_space = text.find(" ", end_idx)
                if next_space != -1 and (next_space - end_idx) < 15:
                    end_idx = next_space

            chunk_content = text[start_idx:end_idx].strip()
            
            if chunk_content:
                chunks.append(DocumentChunk(
                    chunk_id=f"doc-chunk-{chunk_count}",
                    content=chunk_content,
                    page_number=1,
                    metadata={"source_file": "report.pdf"}
                ))
                chunk_count += 1
            
            # Slide window forward by chunk_size minus the overlap offset
            start_idx += (chunk_size - chunk_overlap)
            
            if chunk_size <= chunk_overlap:
                break
                
        return chunks

async def bounded_process(file_path: str, semaphore: asyncio.Semaphore, pipeline: IngestionPipeline) -> List[DocumentChunk]:
    """
    Wraps worker execution inside a semaphore context manager.
    Safely throttles concurrent requests to handle long waiting periods and protect API rate limits.
    """
    async with semaphore:
        parsed_text = await pipeline.simulate_document_intelligence_layout(file_path)
        chunks = await pipeline.chunk_document(parsed_text)
        return chunks

async def main():
    print("🚀 Running Async Ingestion Pipeline Validation Runner...")
    pipeline = IngestionPipeline(index_name="clinical-evidence-index")
    
    # Restrict batch parsing to a maximum of 3 concurrent workers
    concurrency_semaphore = asyncio.Semaphore(3)
    
    # Simulate an incoming batch of multiple documents
    document_batch = [f"financial_report_{i}.pdf" for i in range(1, 5)]
    
    print(f"🚦 Dispatching {len(document_batch)} files concurrently via asyncio.gather...")
    
    # Create concurrent execution tasks
    tasks = [bounded_process(doc, concurrency_semaphore, pipeline) for doc in document_batch]
    
    # Run tasks concurrently, flattening individual network waiting latencies
    batch_results = await asyncio.gather(*tasks)
    
    total_chunks = sum(len(res) for res in batch_results)
    print(f"\n✓ Successfully verified local async ingestion loop. Processed {total_chunks} total chunks across the batch!")

if __name__ == "__main__":
    # Standard entry point to execute our asynchronous event loop
    asyncio.run(main())
