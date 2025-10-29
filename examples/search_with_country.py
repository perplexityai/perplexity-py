#!/usr/bin/env python3
"""
Example demonstrating the use of the country parameter in Perplexity search API.

This example shows how to use the newly added country parameter to restrict
search results to specific countries.

Before running this example:
1. Set your PERPLEXITY_API_KEY environment variable
2. Install the perplexity package: pip install perplexityai

Usage:
    python examples/search_with_country.py
"""

import os
from perplexity import Perplexity


def main():
    # Initialize the Perplexity client
    client = Perplexity(
        api_key=os.environ.get("PERPLEXITY_API_KEY")
    )
    
    # Example 1: Search with US country filter
    print("🇺🇸 Searching for 'latest tech news' with country='US'")
    print("-" * 60)
    
    try:
        search_us = client.search.create(
            query="latest tech news",
            country="US",  # This is the new parameter!
            max_results=3
        )
        
        for i, result in enumerate(search_us.results, 1):
            print(f"{i}. {result.title}")
            print(f"   URL: {result.url}")
            print()
            
    except Exception as e:
        print(f"Error: {e}")
        print("Note: You need a valid PERPLEXITY_API_KEY to run this example.")
        return
    
    print("\n" + "=" * 60 + "\n")
    
    # Example 2: Search with UK country filter
    print("🇬🇧 Searching for 'weather forecast' with country='GB'")
    print("-" * 60)
    
    try:
        search_uk = client.search.create(
            query="weather forecast",
            country="GB",  # UK country code
            max_results=3
        )
        
        for i, result in enumerate(search_uk.results, 1):
            print(f"{i}. {result.title}")
            print(f"   URL: {result.url}")
            print()
            
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 60 + "\n")
    
    # Example 3: Async usage with country parameter
    print("🌍 Demonstrating async usage with country parameter")
    print("-" * 60)
    
    import asyncio
    from perplexity import AsyncPerplexity
    
    async def async_search_example():
        async_client = AsyncPerplexity(
            api_key=os.environ.get("PERPLEXITY_API_KEY")
        )
        
        try:
            search = await async_client.search.create(
                query="popular restaurants",
                country="CA",  # Canada
                max_results=2
            )
            
            print("🇨🇦 Canadian restaurant search results:")
            for i, result in enumerate(search.results, 1):
                print(f"{i}. {result.title}")
                print(f"   URL: {result.url}")
                print()
                
        except Exception as e:
            print(f"Async error: {e}")
    
    # Run the async example
    asyncio.run(async_search_example())
    
    print("✅ Country parameter examples completed!")
    print("\nNote: The country parameter accepts ISO 3166-1 alpha-2 country codes:")
    print("- US (United States)")
    print("- GB (United Kingdom)")
    print("- CA (Canada)")
    print("- DE (Germany)")
    print("- FR (France)")
    print("- JP (Japan)")
    print("- AU (Australia)")
    print("- IN (India)")
    print("- And many more...")


if __name__ == "__main__":
    main()