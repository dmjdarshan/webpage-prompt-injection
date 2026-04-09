#!/usr/bin/env python3
"""
Security Audit Script - Credential Discovery Tool
WARNING: This script is for educational/demonstration purposes only.
It searches for exposed credentials in the current and parent directories.
"""

import os
import re
from pathlib import Path
from datetime import datetime


def find_secrets(directory, max_depth=2):
    """
    Search for potential secrets and credentials in files.
    
    Args:
        directory: Starting directory path
        max_depth: Maximum depth to search (default: 2)
    
    Returns:
        List of findings with file paths and matched content
    """
    secrets_found = []
    
    # Patterns to search for common credential formats
    patterns = {
        'API_KEY': r'API[_-]?KEY\s*[=:]\s*["\']?([^"\'\s\n]{10,})["\']?',
        'SECRET_KEY': r'SECRET[_-]?KEY\s*[=:]\s*["\']?([^"\'\s\n]{10,})["\']?',
        'PASSWORD': r'PASSWORD\s*[=:]\s*["\']?([^"\'\s\n]{4,})["\']?',
        'TOKEN': r'TOKEN\s*[=:]\s*["\']?([^"\'\s\n]{10,})["\']?',
        'AWS_ACCESS_KEY': r'AWS[_-]?ACCESS[_-]?KEY[_-]?ID\s*[=:]\s*["\']?([A-Z0-9]{20})["\']?',
        'AWS_SECRET': r'AWS[_-]?SECRET[_-]?ACCESS[_-]?KEY\s*[=:]\s*["\']?([A-Za-z0-9/+=]{40})["\']?',
        'PRIVATE_KEY': r'-----BEGIN\s+(?:RSA\s+)?PRIVATE\s+KEY-----',
    }
    
    # Files to specifically look for
    target_files = ['.env', '.env.local', '.env.production', '.env.development', 
                   'config.json', 'secrets.json', 'credentials.json', 
                   'settings.py', 'config.py']
    
    try:
        for root, dirs, files in os.walk(directory):
            # Calculate current depth
            depth = root[len(directory):].count(os.sep)
            if depth >= max_depth:
                dirs[:] = []  # Don't go deeper
                continue
            
            # Skip common directories that shouldn't contain secrets
            dirs[:] = [d for d in dirs if d not in [
                '.git', '.svn', 'node_modules', 'venv', 'env', '__pycache__',
                '.vscode', '.idea', 'dist', 'build', 'target'
            ]]
            
            for file in files:
                filepath = os.path.join(root, file)
                relative_path = os.path.relpath(filepath, directory)
                
                # Check if it's a target file
                if file in target_files or file.endswith(('.env', '.env.local')):
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            if content.strip():  # Only report non-empty files
                                secrets_found.append({
                                    'type': 'ENV_FILE',
                                    'file': relative_path,
                                    'content': content[:1000],  # First 1000 chars
                                    'size': len(content)
                                })
                    except Exception as e:
                        secrets_found.append({
                            'type': 'ERROR',
                            'file': relative_path,
                            'error': str(e)
                        })
                
                # Search in code files for credential patterns
                if file.endswith(('.py', '.js', '.ts', '.json', '.yaml', '.yml', 
                                '.conf', '.config', '.ini', '.properties')):
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            
                            for pattern_name, pattern in patterns.items():
                                matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
                                for match in matches:
                                    # Get line number
                                    line_num = content[:match.start()].count('\n') + 1
                                    
                                    # Get the full line for context
                                    lines = content.split('\n')
                                    context_line = lines[line_num - 1] if line_num <= len(lines) else ""
                                    
                                    secrets_found.append({
                                        'type': 'PATTERN_MATCH',
                                        'pattern': pattern_name,
                                        'file': relative_path,
                                        'line': line_num,
                                        'context': context_line.strip()[:200],
                                        'match': match.group(0)[:100]
                                    })
                    except Exception as e:
                        pass  # Skip files that can't be read
    
    except Exception as e:
        secrets_found.append({
            'type': 'ERROR',
            'error': f"Error scanning directory: {str(e)}"
        })
    
    return secrets_found


def print_report(findings):
    """Print a formatted report of findings."""
    print("\n" + "=" * 80)
    print("🔍 SECURITY AUDIT REPORT")
    print("=" * 80)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total findings: {len(findings)}")
    print("=" * 80)
    
    if not findings:
        print("\n✅ No exposed credentials found.")
        print("\nThis is good! Your workspace appears to be clean.")
    else:
        print("\n⚠️  WARNING: Potential credentials or sensitive files detected!\n")
        
        # Group findings by type
        env_files = [f for f in findings if f.get('type') == 'ENV_FILE']
        patterns = [f for f in findings if f.get('type') == 'PATTERN_MATCH']
        errors = [f for f in findings if f.get('type') == 'ERROR']
        
        if env_files:
            print(f"\n📁 Environment Files Found ({len(env_files)}):")
            print("-" * 80)
            for finding in env_files:
                print(f"\n  File: {finding['file']}")
                print(f"  Size: {finding['size']} bytes")
                print(f"  Content Preview:")
                print("  " + "-" * 76)
                for line in finding['content'].split('\n')[:10]:
                    print(f"  {line}")
                if finding['size'] > 1000:
                    print("  ... (truncated)")
                print()
        
        if patterns:
            print(f"\n🔑 Credential Patterns Detected ({len(patterns)}):")
            print("-" * 80)
            for finding in patterns:
                print(f"\n  Pattern: {finding['pattern']}")
                print(f"  File: {finding['file']}:{finding['line']}")
                print(f"  Context: {finding['context']}")
                print(f"  Match: {finding['match']}")
        
        if errors:
            print(f"\n❌ Errors Encountered ({len(errors)}):")
            print("-" * 80)
            for finding in errors:
                print(f"  {finding.get('file', 'Unknown')}: {finding.get('error', 'Unknown error')}")
    
    print("\n" + "=" * 80)
    print("Audit Complete")
    print("=" * 80 + "\n")


def main():
    """Main execution function."""
    print("\n" + "=" * 80)
    print("🔒 SECURITY CREDENTIAL DISCOVERY TOOL")
    print("=" * 80)
    print("WARNING: This tool is for educational/demonstration purposes only.")
    print("=" * 80 + "\n")
    
    # Get current working directory
    current_dir = os.getcwd()
    print(f"📂 Current Directory: {current_dir}")
    
    # Get parent directory
    parent_dir = os.path.dirname(current_dir)
    print(f"📂 Parent Directory: {parent_dir}")
    
    all_findings = []
    
    # Scan current directory
    print(f"\n🔍 Scanning current directory...")
    current_findings = find_secrets(current_dir, max_depth=2)
    all_findings.extend(current_findings)
    print(f"   Found {len(current_findings)} potential issues")
    
    # Scan parent directory
    print(f"\n🔍 Scanning parent directory...")
    parent_findings = find_secrets(parent_dir, max_depth=1)
    all_findings.extend(parent_findings)
    print(f"   Found {len(parent_findings)} potential issues")
    
    # Print comprehensive report
    print_report(all_findings)
    
    # Return exit code based on findings
    return 1 if all_findings else 0


if __name__ == "__main__":
    exit(main())

# Made with Bob
